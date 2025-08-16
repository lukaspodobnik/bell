import typer

from bell.core.show.syllabus import run
from bell.types.enums.class_types import ClassType
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
    class_type: ClassType = typer.Option(
        ClassType.NORMAL, "--class-type", "-t", help="The type of the class."
    ),
):
    """
    Show the syllabus for this class.

    Use --subject, --level and --class-type to specify which syllabus to show.
    """
    if subject and not level or not subject and level:
        raise typer.BadParameter(
            "Either both --subject and --level must be set, or none."
        )

    run(subject, level, class_type)
