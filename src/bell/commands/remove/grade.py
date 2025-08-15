import typer
from typing_extensions import Annotated

from bell.core.remove.grade import run
from bell.types.cmd_args.student import Student
from bell.types.enums.exam_types import ExamType

app = typer.Typer()


@app.command()
def grade(
    student: Annotated[
        Student,
        typer.Argument(
            parser=Student.parser, help='Student name (e.g., "Max Mustermann").'
        ),
    ],
    number: int = typer.Argument(
        help="Number of the exam, (e.g., 1 for the first exam of given type)."
    ),
    exam_type: ExamType = typer.Argument(help="Type of exam (e.g., kurzarbeit)."),
):
    """
    Remove a grade for a student in this class.
    """
    run(student, number, exam_type)
