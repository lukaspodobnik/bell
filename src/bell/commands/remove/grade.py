import typer

from bell.core.remove.grade import run

app = typer.Typer()


@app.command()
def grade():
    run()
