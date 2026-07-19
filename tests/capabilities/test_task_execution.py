from capabilities.execution.core.execution import (
    execution_capability,
)

from tasks.core.task import Task
from tasks.core.task_manager import (
    task_manager,
)


def main():

    print("=" * 50)
    print("Task Execution")
    print("=" * 50)

    task = Task(
        type="execution",
        action="create_workspace"
    )

    result = task_manager.execute(task)

    print()
    print("Estado:")
    print(task.status)

    print()
    print("Resultado:")
    print(result)

    print()
    print("Task:")
    print(task)


if __name__ == "__main__":
    main()
