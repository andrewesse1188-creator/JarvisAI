from gateway.core.gateway import gateway
from research.services.search_service import SearchService


class Agent:

    def __init__(
        self,
        agent_id,
        name,
        role,
        description,
        model,
        skills,
        system_prompt,
        enabled=True
    ):
        self.id = agent_id
        self.name = name
        self.role = role
        self.description = description
        self.model = model
        self.skills = skills
        self.system_prompt = system_prompt
        self.enabled = enabled

        self.search = SearchService()

    def build_research_context(self, query: str):

        if "research" not in self.skills:
            return ""

        try:

            results = self.search.search(
                query=query,
                max_results=5
            )

            if not results:
                return ""

            text = "\n\n"

            for result in results:

                text += (
                    f"Título: {result.title}\n"
                    f"URL: {result.url}\n"
                    f"Resumen: {result.snippet}\n\n"
                )

            return text

        except Exception:

            return ""

    def build_prompt(self, user_prompt: str):

        research = self.build_research_context(user_prompt)

        return f"""
{self.system_prompt}

INFORMACIÓN ENCONTRADA:

{research}

PREGUNTA DEL USUARIO:

{user_prompt}

Responde utilizando la información anterior cuando sea útil.
Si la información no es suficiente, indícalo claramente.
"""

    def execute(self, user_prompt: str):

        prompt = self.build_prompt(user_prompt)

        return gateway.generate(
            prompt=prompt,
            model=self.model,
            provider="ollama"
        )

    def __repr__(self):
        status = "activo" if self.enabled else "inactivo"
        return f"<Agent {self.name} | {self.role} | {status}>"
