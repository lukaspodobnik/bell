import typer

from bell.core.remove.exam import run

app = typer.Typer()


@app.command()
def exam():
    run()
