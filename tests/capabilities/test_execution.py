from capabilities.execution.core.execution import (
    ExecutionCapability
)


def main():

    capability = ExecutionCapability()

    print("=" * 50)
    print("Execution Capability")
    print("=" * 50)

    print("\nHealth")

    print(
        capability.health()
    )

    print("\nCreando Workspace...")

    workspace = capability.execute(
        {
            "type": "execution",
            "action": "create_workspace"
        }
    )

    print(workspace)


if __name__ == "__main__":
    main()
