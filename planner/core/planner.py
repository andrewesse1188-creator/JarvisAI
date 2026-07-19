import json

from gateway.core.gateway import gateway
from agents.core.manager import agent_manager


class IntelligentPlanner:

    VALID_AGENTS = [
        "atlas",
        "orion",
        "athena",
        "sentinel",
        "forge"
    ]

    def plan(self, prompt: str):

        planning_prompt = f"""
Eres el planificador interno de JARVIS.

Debes decidir qué agentes son realmente necesarios para resolver
la petición del usuario.

Agentes disponibles:

atlas:
Arquitectura de software y diseño de sistemas.

orion:
Programación, código y debugging.

athena:
Investigación, análisis y explicaciones generales.

sentinel:
Ciberseguridad y análisis de seguridad.

forge:
Docker, Linux, DevOps e infraestructura.

REGLAS:

1. Usa un solo agente siempre que sea suficiente.
2. Usa varios agentes únicamente para tareas complejas.
3. Máximo 3 agentes.
4. No selecciones agentes que aporten poco valor.
5. Devuelve únicamente JSON válido.

Formato:

{{"agents": ["athena"]}}

PETICIÓN:

{prompt}
"""

        try:

            response = gateway.generate(
                prompt=planning_prompt,
                model="qwen3:8b",
                provider="ollama"
            )

            start = response.find("{")
            end = response.rfind("}") + 1

            if start == -1 or end == 0:
                return []

            data = json.loads(response[start:end])

            selected = []

            for agent_id in data.get("agents", [])[:3]:

                if agent_id not in self.VALID_AGENTS:
                    continue

                agent = agent_manager.get_agent(agent_id)

                if agent and agent.enabled:
                    selected.append(agent)

            return selected

        except Exception:
            return []


intelligent_planner = IntelligentPlanner()
