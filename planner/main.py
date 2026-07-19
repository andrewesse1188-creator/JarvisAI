from dispatcher.model_selector import select_model


class Planner:

    def analyze(self, prompt: str):

        model = select_model(prompt)

        return {
            "prompt": prompt,
            "model": model
        }


planner = Planner()
