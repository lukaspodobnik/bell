import typer

from bell.core.show.syllabus import run
from bell.types.enums.subjects import Subject

app = typer.Typer()


@app.command()
def syllabus(
    subject: Subject = typer.Option(
        None, "--subject", "-s", help="The subject of the syllabus."
    ),
    level: int = typer.Option(
        None, "--level", "-l", help="The grade-level of the syllabus."
    ),
):
    """
    Show the syllabus for this class.

    Use --subject and --level to specify which syllabus to show.
    """
    if subject and not level or not subject and level:
        raise typer.BadParameter("Either both options or none must be set.")

    run(subject, level)
