from research.core.gateway import ResearchGateway
from research.models.search_result import SearchResult


class SearchService:
    """
    Servicio de búsqueda utilizado por JARVIS.
    """

    def __init__(self):
        self.gateway = ResearchGateway()

    def search(self, query: str, max_results: int = 5) -> list[SearchResult]:
        return self.gateway.search(
            query=query,
            max_results=max_results,
        )
