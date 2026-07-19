from brain.services.ollama import list_models


def select_model(task: str) -> str:
    """
    Selecciona automáticamente el mejor modelo.
    """

    task = task.lower()

    models = list_models()

    if "program" in task or "python" in task or "codigo" in task:
        if "qwen2.5-coder:7b" in models:
            return "qwen2.5-coder:7b"

    if "investigar" in task or "explicar" in task:
        if "deepseek-r1:8b" in models:
            return "deepseek-r1:8b"

    return "qwen3:8b"
