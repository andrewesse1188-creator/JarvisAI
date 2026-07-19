from gateway.providers.ollama import generate as ollama_generate


class ModelGateway:

    def generate(
        self,
        prompt: str,
        model: str = "qwen3:8b",
        provider: str = "ollama"
    ) -> str:

        if provider == "ollama":
            return ollama_generate(
                prompt=prompt,
                model=model
            )

        raise ValueError(
            f"Proveedor no disponible: {provider}"
        )


gateway = ModelGateway()
