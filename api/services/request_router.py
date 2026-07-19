class OpenWebUIRequestRouter:

    AUXILIARY_MARKERS = (
        "### Task:",
        "Generate a concise, 3-5 word title",
        "Suggest 3-5 relevant follow-up",
        "Generate 1-3 broad tags",
    )

    def is_auxiliary(self, prompt: str) -> bool:
        return any(
            marker.lower() in prompt.lower()
            for marker in self.AUXILIARY_MARKERS
        )


request_router = OpenWebUIRequestRouter()
