import typer

from bell.commands.add import app as add_app
from bell.commands.init import app as init_app
from bell.commands.show import app as show_app


def main() -> None:
    app = typer.Typer()

    app.add_typer(init_app, name="init")
    app.add_typer(add_app, name="add")
    app.add_typer(show_app, name="show")

    app()
