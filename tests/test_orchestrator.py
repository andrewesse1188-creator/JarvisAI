from orchestrator.core.orchestrator import orchestrator


prompt = "Diseña y programa una API REST segura usando Python y FastAPI."

print("=" * 60)
print("JARVIS MULTI-AGENT TEST")
print("=" * 60)

print(f"\nPregunta: {prompt}")

results = orchestrator.process(prompt)

for result in results:

    print("\n" + "=" * 60)
    print(f"AGENTE: {result['agent']}")
    print(f"ROL: {result['role']}")
    print("=" * 60)

    print(result["response"])
