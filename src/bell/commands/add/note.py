import typer

from bell.core.add.note import run

app = typer.Typer()


@app.command()
def note():
    run()
