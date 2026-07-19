from research.core.router import ResearchRouter


class ResearchGateway:
    """
    Punto único de acceso al módulo de investigación.
    """

    def __init__(self):
        self.router = ResearchRouter()

    def search(
        self,
        query: str,
        provider: str = "duckduckgo",
        max_results: int = 5,
    ):
        engine = self.router.get_provider(provider)

        if engine is None:
            raise ValueError(f"Proveedor '{provider}' no encontrado.")

        return engine.search(
            query=query,
            max_results=max_results,
        )
