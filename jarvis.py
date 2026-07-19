from core.application import app
from conversation.main import engine

app.start()

print("=" * 60)
print("JARVIS ENGINEERING AI")
print("=" * 60)

while True:

    try:
        pregunta = input("\nTú > ")

        if pregunta.lower() in ["salir", "exit", "quit"]:
            break

        respuesta = engine.process(pregunta)

        print("\nJARVIS >")
        print(respuesta)

    except KeyboardInterrupt:
        print("\n\nInterrupción recibida.")
        break

app.stop()
