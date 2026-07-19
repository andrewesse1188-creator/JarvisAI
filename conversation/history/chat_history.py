class ChatHistory:

    def __init__(self, max_messages=10):
        self.messages = []
        self.max_messages = max_messages

    def add(self, role, content):

        self.messages.append({
            "role": role,
            "content": str(content)
        })

        # Conservamos solo los últimos mensajes
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

    def all(self):
        return self.messages.copy()

    def context(self):

        if not self.messages:
            return ""

        lines = []

        for message in self.messages:
            role = message["role"]

            if role == "user":
                name = "Usuario"
            else:
                name = "JARVIS"

            lines.append(
                f"{name}: {message['content']}"
            )

        return "\n\n".join(lines)

    def clear(self):
        self.messages.clear()


history = ChatHistory(max_messages=10)
