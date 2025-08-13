import typer

from bell.core.remove.lesson import run

app = typer.Typer()


@app.command()
def lesson():
    run()
