from abc import ABC, abstractmethod


class BaseRunner(ABC):

    def __init__(self, name: str):

        self.name = name

    @abstractmethod
    def can_run(
        self,
        task: dict
    ) -> bool:
        pass

    @abstractmethod
    def run(
        self,
        task: dict
    ):
        pass

    def health(self):

        return {
            "runner": self.name,
            "status": "ready"
        }

    def __repr__(self):

        return (
            f"<Runner {self.name}>"
        )
