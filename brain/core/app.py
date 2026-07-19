from brain.services.ollama import check_connection, list_models


def main():

    print("=" * 50)
    print("JARVIS ENGINEERING AI")
    print("=" * 50)

    if check_connection():

        print("[OK] Ollama conectado")

        models = list_models()

        if models:

            print("\nModelos encontrados:")

            for model in models:
                print(f" - {model}")

        else:

            print("No hay modelos instalados.")

    else:

        print("[ERROR] No se pudo conectar con Ollama.")


if __name__ == "__main__":
    main()
