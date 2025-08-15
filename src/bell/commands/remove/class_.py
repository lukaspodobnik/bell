import typer

from bell.core.remove.class_ import run

app = typer.Typer()

app.command()


def class_():
    run()
