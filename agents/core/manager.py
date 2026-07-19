from agents.registry.registry import registry


class AgentManager:

    def list_agents(self):
        return registry.list_agents()

    def get_agent(self, agent_id):
        return registry.get(agent_id)

    def get_active_agents(self):
        return registry.get_active()

    def find_agents_by_skill(self, skill):
        return registry.find_by_skill(skill)

    def reload(self):
        registry.reload()


agent_manager = AgentManager()
