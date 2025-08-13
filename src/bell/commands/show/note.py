import typer

from bell.core.show.note import run

app = typer.Typer()


@app.command()
def note():
    run()
