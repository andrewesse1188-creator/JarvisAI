from conversation.history.chat_history import history
from orchestrator.core.orchestrator import orchestrator


class ConversationEngine:

    def process(self, prompt: str):

        # Recuperamos el contexto anterior.
        previous_context = history.context()

        # Guardamos la pregunta actual.
        history.add("user", prompt)

        # Enviamos por separado:
        # prompt = mensaje actual
        # context = conversación anterior
        response = orchestrator.process(
            prompt=prompt,
            context=previous_context
        )

        # Guardamos la respuesta.
        history.add(
            "assistant",
            response
        )

        return response

    def clear_history(self):
        history.clear()


engine = ConversationEngine()
