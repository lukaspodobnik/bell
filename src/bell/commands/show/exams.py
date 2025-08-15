import typer

from bell.core.show.exams import run

app = typer.Typer()


@app.command()
def exams():
    run()
