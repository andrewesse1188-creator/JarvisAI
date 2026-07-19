from agents.core.manager import agent_manager
from gateway.core.gateway import gateway


class ResponseSynthesizer:

    def synthesize(self, prompt, results):

        if not results:
            return "No se pudo generar una respuesta."

        # Si solo trabajó un agente, devolvemos directamente su respuesta.
        # Esto evita una llamada adicional al modelo.
        if len(results) == 1:
            return results[0]["response"]

        aegis = agent_manager.get_agent("aegis")

        if not aegis or not aegis.enabled:
            return "\n\n".join(
                result["response"]
                for result in results
            )

        agent_responses = ""

        for result in results:
            agent_responses += f"""
AGENTE: {result['agent']}
ROL: {result['role']}

RESPUESTA:
{result['response']}

------------------------------
"""

        verification_prompt = f"""
{aegis.system_prompt}

PETICIÓN ORIGINAL DEL USUARIO:
{prompt}

RESPUESTAS DE LOS AGENTES:
{agent_responses}

INSTRUCCIONES:

Analiza las respuestas de los agentes.

Combina únicamente la información útil.

Elimina repeticiones.

Corrige contradicciones evidentes.

No menciones el proceso interno ni los nombres de los agentes.

Entrega una única respuesta final, clara y bien estructurada.

RESPUESTA FINAL:
"""

        return gateway.generate(
            prompt=verification_prompt,
            model=aegis.model,
            provider="ollama"
        )


response_synthesizer = ResponseSynthesizer()
