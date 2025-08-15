import typer

from bell.core.show.students import run

app = typer.Typer()


@app.command()
def students():
    """
    Show all students in this class.
    """
    run()
