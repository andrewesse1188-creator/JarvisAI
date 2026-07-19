import requests

OLLAMA_URL = "http://127.0.0.1:11434"


def generate(prompt: str, model: str = "qwen3:8b") -> str:
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        },
        timeout=300
    )

    response.raise_for_status()

    data = response.json()
    return data["response"]
