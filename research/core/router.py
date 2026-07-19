from research.providers.duckduckgo import DuckDuckGoProvider
from research.providers.github import GitHubProvider
from research.providers.wikipedia import WikipediaProvider


class ResearchRouter:
    """
    Router encargado de decidir qué proveedor utilizar.
    """

    def __init__(self):
        self.providers = {
            "duckduckgo": DuckDuckGoProvider(),
            "github": GitHubProvider(),
            "wikipedia": WikipediaProvider(),
        }

    def get_provider(self, provider: str = "duckduckgo"):
        return self.providers.get(provider)
