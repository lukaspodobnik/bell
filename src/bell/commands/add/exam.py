import typer

from bell.core.add.exam import run

app = typer.Typer()


@app.command()
def exam():
    run()
