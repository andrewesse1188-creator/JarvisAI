from abc import ABC, abstractmethod


class Capability(ABC):
    """
    Clase base para todas las capacidades de JarvisAI.

    Ninguna capacidad debe modificar el proyecto
    directamente. Todas trabajan mediante el
    CapabilityManager.
    """

    def __init__(
        self,
        capability_id: str,
        name: str,
        version: str = "1.0.0",
        enabled: bool = True
    ):

        self.id = capability_id
        self.name = name
        self.version = version
        self.enabled = enabled

    @abstractmethod
    def can_execute(
        self,
        task: dict
    ) -> bool:
        pass

    @abstractmethod
    def execute(
        self,
        task: dict
    ):
        pass

    def health(self):

        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "enabled": self.enabled
        }

    def __repr__(self):

        state = "enabled" if self.enabled else "disabled"

        return (
            f"<Capability "
            f"{self.name} "
            f"v{self.version} "
            f"{state}>"
        )
