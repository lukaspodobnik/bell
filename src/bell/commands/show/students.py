import typer

from bell.core.show.students import run

app = typer.Typer()


@app.command()
def students():
    run()
