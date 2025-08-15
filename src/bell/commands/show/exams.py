import typer

from bell.core.show.exams import run

app = typer.Typer()


@app.command()
def exams():
    """
    Show all planned (and already completed) exams for this class.
    """
    run()
