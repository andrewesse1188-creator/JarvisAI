from dataclasses import dataclass
from typing import Optional


@dataclass
class SearchResult:
    """
    Representa un resultado de búsqueda obtenido desde cualquier proveedor.
    """

    title: str
    url: str
    snippet: str

    provider: str

    score: float = 0.0

    published: Optional[str] = None
