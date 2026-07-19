import requests

from research.models.search_result import SearchResult
from research.providers.base_provider import BaseProvider


class GitHubProvider(BaseProvider):
    name = "github"

    def search(self, query: str, max_results: int = 5):
        url = "https://api.github.com/search/repositories"

        response = requests.get(
            url,
            params={
                "q": query,
                "per_page": max_results,
            },
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        results = []

        for repo in data.get("items", []):
            results.append(
                SearchResult(
                    title=repo["full_name"],
                    url=repo["html_url"],
                    snippet=repo.get("description") or "",
                    provider=self.name,
                    score=0.90,
                )
            )

        return results
