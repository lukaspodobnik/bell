import typer
from typing_extensions import Annotated

from bell.core.show.grades import run
from bell.types.cmd_args.student import Student
from bell.types.enums.exam_types import ExamType

app = typer.Typer()


@app.command()
def grades(
    student: Annotated[
        Student,
        typer.Option(
            "--student",
            "-s",
            parser=Student.parser,
            help="The student to show grades for (e.g. 'Max Mustermann').",
        ),
    ] = None,
    exam_type: ExamType = typer.Option(
        None, "--exam-type", "-t", help="Type of the exam (e.g., kurzarbeit)."
    ),
    last: bool = typer.Option(
        False,
        "--last",
        "-l",
        help="Set this to only show the grades for the last exam.",
    ),
):
    """
    Show grades for this class.

    Use --student to only show grades for a specific student.
    Use --exam-type to only show grades for a specific exam type.
    Use --last to only show the grads for the last exam.
    """
    if (
        (student and (exam_type or last))
        or (exam_type and (student or last))
        or (last and (student or exam_type))
    ):
        raise typer.BadParameter(
            "Please provide only one of the options: --student, --exam-type, --last."
        )

    run(student, exam_type, last)
