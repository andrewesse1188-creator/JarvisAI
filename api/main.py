import json
import time
import uuid

from typing import List, Optional

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from conversation.main import engine
from resources.manager import resource_manager
from api.services.request_router import request_router
from gateway.core.gateway import gateway
from orchestrator.core.orchestrator import orchestrator


app = FastAPI(
    title="JARVIS AI API",
    description="API del sistema multiagente JARVIS",
    version="0.3.0"
)


# ============================================================
# API NATIVA DE JARVIS
# ============================================================

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.get("/")
def root():
    return {
        "name": "JARVIS AI",
        "version": "0.3.0",
        "status": "online"
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "resources": resource_manager.get_status()
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    response = engine.process(
        request.message
    )

    return ChatResponse(
        response=response
    )


@app.delete("/memory")
def clear_memory():

    engine.clear_history()

    return {
        "status": "ok",
        "message": "Memoria de conversación eliminada"
    }


# ============================================================
# COMPATIBILIDAD OPENAI / OPEN WEBUI
# ============================================================

class OpenAIMessage(BaseModel):
    role: str
    content: str


class OpenAIChatRequest(BaseModel):
    model: Optional[str] = "jarvis"
    messages: List[OpenAIMessage]
    stream: Optional[bool] = False


@app.get("/v1/models")
def openai_models():

    return {
        "object": "list",
        "data": [
            {
                "id": "jarvis",
                "object": "model",
                "created": int(time.time()),
                "owned_by": "jarvis-ai"
            }
        ]
    }


# ============================================================
# STREAMING COMPATIBLE CON OPENAI / OPEN WEBUI
# ============================================================

def generate_stream(response: str):

    completion_id = f"chatcmpl-{uuid.uuid4().hex}"

    chunk = {
        "id": completion_id,
        "object": "chat.completion.chunk",
        "created": int(time.time()),
        "model": "jarvis",
        "choices": [
            {
                "index": 0,
                "delta": {
                    "role": "assistant",
                    "content": response
                },
                "finish_reason": None
            }
        ]
    }

    yield (
        f"data: "
        f"{json.dumps(chunk, ensure_ascii=False)}"
        f"\n\n"
    )

    final_chunk = {
        "id": completion_id,
        "object": "chat.completion.chunk",
        "created": int(time.time()),
        "model": "jarvis",
        "choices": [
            {
                "index": 0,
                "delta": {},
                "finish_reason": "stop"
            }
        ]
    }

    yield (
        f"data: "
        f"{json.dumps(final_chunk, ensure_ascii=False)}"
        f"\n\n"
    )

    yield "data: [DONE]\n\n"


# ============================================================
# ENDPOINT PRINCIPAL OPENAI-COMPATIBLE
# ============================================================

@app.post("/v1/chat/completions")
def openai_chat(request: OpenAIChatRequest):

    print("\n" + "=" * 70)
    print("[JARVIS API] Nueva solicitud OpenAI-compatible")
    print(f"Modelo: {request.model}")
    print(f"Streaming: {request.stream}")

    for message in request.messages:
        print(
            f"[{message.role}] "
            f"{message.content[:500]}"
        )

    print("=" * 70 + "\n")

    # --------------------------------------------------------
    # OBTENER LOS MENSAJES DEL USUARIO
    # --------------------------------------------------------

    user_messages = [
        message.content
        for message in request.messages
        if message.role == "user"
    ]

    if not user_messages:

        return {
            "error": {
                "message": (
                    "No se encontró un mensaje "
                    "del usuario."
                )
            }
        }

    # El último mensaje del usuario es la petición actual.
    prompt = user_messages[-1]

    # --------------------------------------------------------
    # DETECTAR SOLICITUDES AUXILIARES DE OPEN WEBUI
    # --------------------------------------------------------

    if request_router.is_auxiliary(prompt):

        print(
            "[JARVIS API] "
            "Solicitud auxiliar detectada"
        )

        # Las tareas internas de Open WebUI
        # NO pasan por la memoria de conversación.
        response = gateway.generate(
            prompt=prompt,
            model="qwen3:8b",
            provider="ollama"
        )

    else:

        print(
            "[JARVIS API] "
            "Conversación principal detectada"
        )

        # ----------------------------------------------------
        # CONSTRUIR CONTEXTO DE LA CONVERSACIÓN ACTUAL
        # ----------------------------------------------------
        #
        # Open WebUI envía el historial de la conversación
        # dentro de request.messages.
        #
        # Por eso usamos ese historial directamente.
        #
        # Esto evita que diferentes chats de Open WebUI
        # compartan el objeto global "history".
        # ----------------------------------------------------

        conversation_context = []

        # Excluimos el último mensaje porque ese mensaje
        # ya está almacenado en la variable "prompt".
        for message in request.messages[:-1]:

            if message.role in [
                "user",
                "assistant"
            ]:

                conversation_context.append(
                    f"{message.role.upper()}: "
                    f"{message.content}"
                )

        # Limitamos el contexto a los últimos 10 mensajes
        # para evitar enviar historiales demasiado grandes
        # a los modelos locales.
        context = "\n\n".join(
            conversation_context[-10:]
        )

        # La conversación web pasa directamente
        # al Orchestrator con su propio contexto.
        #
        # No usamos engine.process() aquí porque
        # ConversationEngine utiliza actualmente
        # un historial global.
        response = orchestrator.process(
            prompt=prompt,
            context=context
        )

    # --------------------------------------------------------
    # RESPUESTA STREAMING
    # --------------------------------------------------------

    if request.stream:

        return StreamingResponse(
            generate_stream(response),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive"
            }
        )

    # --------------------------------------------------------
    # RESPUESTA OPENAI ESTÁNDAR SIN STREAMING
    # --------------------------------------------------------

    return {
        "id": f"chatcmpl-{uuid.uuid4().hex}",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": "jarvis",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": response
                },
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0
        }
    }
