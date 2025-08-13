import typer

from bell.core.show.grades import run

app = typer.Typer()


@app.command()
def grades():
    run()
