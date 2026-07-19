class TaskRegistry:

    def __init__(self):

        self._tasks = {}

    def register(self, task):

        self._tasks[task.id] = task

    def get(self, task_id):

        return self._tasks.get(task_id)

    def all(self):

        return list(
            self._tasks.values()
        )


task_registry = TaskRegistry()

