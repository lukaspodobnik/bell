import typer

from bell.core.show.syllabus import run
from bell.types.enums.subjects import Subject

app = typer.Typer()


@app.command()
def syllabus(
    subject: Subject = typer.Option(None, "--subject", "-s", help=""),
    level: int = typer.Option(None, "--level", "-l", help=""),
):
    if subject and not level or not subject and level:
        raise typer.BadParameter("Either both options or none must be set.")
    
    run(subject, level)
