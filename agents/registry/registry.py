from agents.core.loader import load_agents


class AgentRegistry:

    def __init__(self):
        self.agents = {}
        self.reload()

    def reload(self):
        self.agents = load_agents()

    def get(self, agent_id):
        return self.agents.get(agent_id)

    def get_active(self):
        return {
            agent_id: agent
            for agent_id, agent in self.agents.items()
            if agent.enabled
        }

    def find_by_skill(self, skill):
        return [
            agent
            for agent in self.get_active().values()
            if skill.lower() in [s.lower() for s in agent.skills]
        ]

    def list_agents(self):
        return list(self.agents.values())


registry = AgentRegistry()
