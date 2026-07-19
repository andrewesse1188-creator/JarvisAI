import wikipedia

from research.models.search_result import SearchResult
from research.providers.base_provider import BaseProvider


class WikipediaProvider(BaseProvider):
    name = "wikipedia"

    def search(self, query: str, max_results: int = 5):
        wikipedia.set_lang("es")
        results = []

        try:
            titles = wikipedia.search(query, results=max_results)

            for title in titles:
                page = wikipedia.page(title, auto_suggest=False)

                results.append(
                    SearchResult(
                        title=page.title,
                        url=page.url,
                        snippet=page.summary[:300],
                        provider=self.name,
                        score=0.95,
                    )
                )

        except Exception as e:
            print(f"[Wikipedia Error] {e}")

        return results
