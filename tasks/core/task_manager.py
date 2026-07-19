from capabilities.core.manager import (
    capability_manager
)

from tasks.core.task_registry import (
    task_registry
)


class TaskManager:

    def register(
        self,
        task
    ):

        task_registry.register(task)

    def get(
        self,
        task_id
    ):

        return task_registry.get(task_id)

    def tasks(self):

        return task_registry.all()

    def execute(
        self,
        task
    ):

        self.register(task)

        for capability in capability_manager.enabled():

            if capability.can_execute(task.__dict__):

                result = capability.execute(
                    task.__dict__
                )

                task.status = "completed"

                task.result = result

                return result

        task.status = "failed"

        task.error = (
            "No existe una Capability "
            "compatible."
        )

        return None


task_manager = TaskManager()
