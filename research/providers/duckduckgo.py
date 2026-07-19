from ddgs import DDGS

from research.models.search_result import SearchResult
from research.providers.base_provider import BaseProvider


class DuckDuckGoProvider(BaseProvider):
    """
    Proveedor de búsqueda usando DDGS.
    """

    name = "duckduckgo"

    def search(self, query: str, max_results: int = 5):
        results = []

        try:
            with DDGS() as ddgs:
                response = ddgs.text(query, max_results=max_results)

                for item in response:
                    results.append(
                        SearchResult(
                            title=item.get("title", ""),
                            url=item.get("href", ""),
                            snippet=item.get("body", ""),
                            provider=self.name,
                            score=1.0,
                        )
                    )

        except Exception as e:
            print(f"[Research Error] {e}")

        return results
