from tasks.core.task import Task
from tasks.core.task_manager import task_manager


def main():

    task = Task(
        type="execution",
        action="create_workspace"
    )

    task_manager.register(task)

    print("=" * 50)

    print(task)

    print("=" * 50)

    print(task_manager.tasks())


if __name__ == "__main__":
    main()
