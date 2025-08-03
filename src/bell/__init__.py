import typer

from bell.commands import init


def main() -> None:
    app = typer.Typer()
    app.add_typer(init.app, name="init")
    app()
