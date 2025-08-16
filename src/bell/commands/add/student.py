import typer
from typing_extensions import Annotated

from bell.core.add.student import run
from bell.types.cmd_args.student import Student

app = typer.Typer()


@app.command()
def student(
    student: Annotated[
        Student,
        typer.Argument(
            parser=Student.parser,
            help="The Student to add.",
        ),
    ] = None,
    multiple: bool = typer.Option(
        False,
        "--multiple",
        "-m",
        help="Set this to add multiple students.",
    ),
):
    """
    Add a student (or multiple students) to the current class.

    Adds a single student or --multiple students to the class roster,
    making them available for other commands.
    """

    if student and multiple:
        raise typer.BadParameter(
            "If a student is provided, --multiple flag must not be set."
        )

    if not student and not multiple:
        raise typer.BadParameter(
            "If no student is provided, --multiple flag has to be set."
        )

    run(student)
