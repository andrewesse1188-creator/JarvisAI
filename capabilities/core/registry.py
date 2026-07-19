class CapabilityRegistry:

    def __init__(self):

        self._capabilities = {}

    def register(self, capability):

        self._capabilities[
            capability.id
        ] = capability

    def unregister(
        self,
        capability_id
    ):

        self._capabilities.pop(
            capability_id,
            None
        )

    def get(
        self,
        capability_id
    ):

        return self._capabilities.get(
            capability_id
        )

    def all(self):

        return list(
            self._capabilities.values()
        )

    def enabled(self):

        return [
            capability
            for capability in self._capabilities.values()
            if capability.enabled
        ]


capability_registry = CapabilityRegistry()
