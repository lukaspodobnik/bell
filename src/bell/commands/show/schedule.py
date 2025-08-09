import typer

from bell.core.show.schedule import run

app = typer.Typer()


@app.command()
def schedule():
    run()
