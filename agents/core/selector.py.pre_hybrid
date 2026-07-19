from agents.core.manager import agent_manager


class AgentSelector:

    def _get(self, agent_id):
        agent = agent_manager.get_agent(agent_id)

        if agent and agent.enabled:
            return agent

        return None

    def select(self, prompt: str):

        text = prompt.lower().strip()

        # Programación
        if any(word in text for word in [
            "programa", "programar", "código", "codigo",
            "python", "fastapi", "javascript",
            "debug", "error de código", "error de codigo"
        ]):
            agent = self._get("orion")
            return [agent] if agent else []

        # Ciberseguridad
        if any(word in text for word in [
            "ciberseguridad", "vulnerabilidad",
            "seguridad informática", "seguridad informatica",
            "firewall", "malware", "phishing", "pentesting"
        ]):
            agent = self._get("sentinel")
            return [agent] if agent else []

        # DevOps
        if any(word in text for word in [
            "docker", "ubuntu", "linux",
            "servidor", "devops", "despliegue"
        ]):
            agent = self._get("forge")
            return [agent] if agent else []

        # Arquitectura
        if any(word in text for word in [
            "arquitectura de software",
            "diseña una arquitectura",
            "diseñar una arquitectura",
            "microservicios",
            "diseño de sistema"
        ]):
            agent = self._get("atlas")
            return [agent] if agent else []

        # Peticiones complejas o ambiguas:
        # usamos el Planner IA.
        complex_words = [
            "proyecto completo",
            "sistema completo",
            "plataforma empresarial",
            "proyecto empresarial",
            "solución completa",
            "solucion completa",
            "analiza y desarrolla",
            "diseña y desarrolla"
        ]

        if any(word in text for word in complex_words):

            from planner.core.planner import intelligent_planner

            agents = intelligent_planner.plan(prompt)

            if agents:
                return agents

        # Consulta general
        agent = self._get("athena")

        return [agent] if agent else []


agent_selector = AgentSelector()
