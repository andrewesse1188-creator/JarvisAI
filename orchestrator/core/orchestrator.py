from agents.core.selector import agent_selector
from agents.core.synthesizer import response_synthesizer
from resources.manager import resource_manager


class Orchestrator:

    def process(self, prompt: str, context: str = ""):

        # El selector decide qué agentes participarán
        agents = agent_selector.select(prompt)

        max_agents = resource_manager.recommended_agents()

        if max_agents == 0:
            return (
                "La temperatura o carga del sistema es demasiado alta "
                "para iniciar una tarea pesada en este momento."
            )

        agents = agents[:max_agents]

        results = []

        for agent in agents:

            if resource_manager.recommended_agents() == 0:
                break

            full_prompt = f"""
{agent.system_prompt}

CONTEXTO RECIENTE DE LA CONVERSACIÓN:
{context if context else "No hay contexto anterior."}

PETICIÓN ACTUAL DEL USUARIO:
{prompt}

INSTRUCCIONES:
Responde principalmente a la petición actual.
Usa el contexto anterior solo cuando sea relevante.
Si el usuario hace referencia a algo mencionado anteriormente,
utiliza el contexto para comprender esa referencia.
No repitas innecesariamente el historial.
Responde directamente.
Trabaja desde tu especialidad.

RESPUESTA:
"""

            try:

                response = agent.execute(full_prompt)

                results.append(
                    {
                        "agent": agent.name,
                        "role": agent.role,
                        "model": agent.model,
                        "response": response,
                    }
                )

            except Exception as error:

                print(
                    f"[JARVIS] Error ejecutando "
                    f"{agent.name}: {error}"
                )

        return response_synthesizer.synthesize(
            prompt,
            results,
        )


orchestrator = Orchestrator()
