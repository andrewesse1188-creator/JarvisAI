from engine.runners.base_runner import BaseRunner


class DummyRunner(BaseRunner):

    def __init__(self):

        super().__init__("Dummy")

    def can_run(
        self,
        task
    ):

        return True

    def run(
        self,
        task
    ):

        return {
            "ok": True
        }


def main():

    runner = DummyRunner()

    print("=" * 50)

    print(runner)

    print(runner.health())

    print(runner.run({}))


if __name__ == "__main__":
    main()
