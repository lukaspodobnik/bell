import typer

from bell.commands.init import app as init_app


def main() -> None:
    app = typer.Typer()
    app.add_typer(init_app, name="init")
    app()
