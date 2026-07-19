from capabilities.core.registry import (
    capability_registry
)


class CapabilityManager:

    def register(
        self,
        capability
    ):

        capability_registry.register(
            capability
        )

    def unregister(
        self,
        capability_id
    ):

        capability_registry.unregister(
            capability_id
        )

    def get(
        self,
        capability_id
    ):

        return capability_registry.get(
            capability_id
        )

    def capabilities(self):

        return capability_registry.all()

    def enabled(self):

        return capability_registry.enabled()

    def health(self):

        return [
            capability.health()
            for capability
            in capability_registry.enabled()
        ]


capability_manager = CapabilityManager()
