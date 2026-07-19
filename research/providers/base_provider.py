from abc import ABC, abstractmethod
from typing import List

from research.models.search_result import SearchResult


class BaseProvider(ABC):
    """
    Clase base para todos los proveedores de búsqueda.
    """

    name: str = "base"

    @abstractmethod
    def search(
        self,
        query: str,
        max_results: int = 5
    ) -> List[SearchResult]:
        """
        Ejecuta una búsqueda y devuelve una lista de SearchResult.
        """
        pass
