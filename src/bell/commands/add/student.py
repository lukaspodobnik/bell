import typer
from typing_extensions import Annotated

from bell.core.add.student import run
from bell.types.cmd_args.add import Student

app = typer.Typer()


@app.command()
def student(
    student: Annotated[
        Student, typer.Argument(parser=Student.parser, help="Student help")
    ] = None,
    multiple: bool = typer.Option(
        False,
        "--multiple",
        "-m",
        help="Add many students in an interactive mode. Exit with q.",
    ),
):
    """
    This is how to use the bell add student cmd.
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
