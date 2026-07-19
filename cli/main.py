import typer

from brain.services.ollama import check_connection, list_models

app = typer.Typer(help="JARVIS Engineering AI")


@app.command("status")
def status():
    """Muestra el estado del sistema."""

    typer.echo("=" * 50)
    typer.echo("JARVIS ENGINEERING AI")
    typer.echo("=" * 50)

    if check_connection():
        typer.secho("✓ Ollama conectado", fg=typer.colors.GREEN)

        typer.echo("\nModelos instalados:")

        for model in list_models():
            typer.echo(f" • {model}")

    else:
        typer.secho("✗ No se pudo conectar con Ollama", fg=typer.colors.RED)


def main():
    app()


if __name__ == "__main__":
    main()
