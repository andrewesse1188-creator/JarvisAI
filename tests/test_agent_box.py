from agents.core.manager import agent_manager


print("=" * 60)
print("JARVIS AGENT BOX")
print("=" * 60)

agents = agent_manager.list_agents()

for agent in agents:

    print()
    print(f"ID: {agent.id}")
    print(f"Nombre: {agent.name}")
    print(f"Rol: {agent.role}")
    print(f"Modelo: {agent.model}")
    print(f"Estado: {'ACTIVO' if agent.enabled else 'INACTIVO'}")
    print(f"Skills: {', '.join(agent.skills)}")
