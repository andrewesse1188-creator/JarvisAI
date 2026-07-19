from capabilities.core.capability import Capability
from capabilities.core.manager import capability_manager

from tools.core.manager import tool_manager
from tools.core.workspace import workspace_manager


class ExecutionCapability(Capability):

    def __init__(self):

        super().__init__(
            capability_id="execution",
            name="Execution Capability",
            version="1.0.0"
        )

    def can_execute(
        self,
        task: dict
    ) -> bool:

        return (
            task.get("type")
            == "execution"
        )

    def execute(
        self,
        task: dict
    ):

        action = task.get("action")

        if action == "create_workspace":

            return (
                workspace_manager
                .create_workspace()
            )

        if action == "inspect_file":

            return tool_manager.inspect(
                task["file"]
            )

        if action == "read_file":

            return tool_manager.read_file(
                task["file"]
            )

        raise ValueError(
            f"Acción desconocida: {action}"
        )


execution_capability = ExecutionCapability()

capability_manager.register(
    execution_capability
)
