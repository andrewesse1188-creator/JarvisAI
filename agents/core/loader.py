from pathlib import Path
import yaml

from agents.core.agent import Agent


PROFILES_DIR = Path(__file__).resolve().parent.parent / "profiles"


def load_agents():

    agents = {}

    for profile_path in sorted(PROFILES_DIR.glob("*.yaml")):

        with open(profile_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        if not data:
            continue

        agent = Agent(
            agent_id=data["id"],
            name=data["name"],
            role=data["role"],
            description=data.get("description", ""),
            model=data["model"],
            skills=data.get("skills", []),
            system_prompt=data.get("system_prompt", ""),
            enabled=data.get("enabled", True)
        )

        agents[agent.id] = agent

    return agents
