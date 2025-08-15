import typer
from typing_extensions import Annotated

from bell.core.remove.student import run
from bell.types.cmd_args.student import Student

app = typer.Typer()


@app.command()
def student(
    student: Annotated[
        Student,
        typer.Argument(
            parser=Student.parser,
            help="The student to remove (e.g., 'Max Mustermann').",
        ),
    ],
) -> None:
    """
    Remove a student from this class.
    """
    run(student)
