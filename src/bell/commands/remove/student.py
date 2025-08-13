import typer

from bell.core.remove.student import run

app = typer.Typer()


@app.command()
def student():
    run()
