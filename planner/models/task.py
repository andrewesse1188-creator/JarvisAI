from dataclasses import dataclass


@dataclass
class Task:
    action: str
    target: str
    confidence: float = 1.0
