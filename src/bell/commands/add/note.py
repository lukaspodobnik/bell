import typer

from bell.core.add.note import run

app = typer.Typer()


@app.command()
def note():
    """
    Add a note for the current class.

    Prompts for the content of the note in the terminal and saves it as a markdown
    file under the class's notes folder for later reference.
    """
    run()
