from datetime import datetime

import typer
from typing_extensions import Annotated

from bell.core.add.grade import run
from bell.types.cmd_args.date import Date
from bell.types.cmd_args.student import Student
from bell.types.enums.exam_types import ExamType

app = typer.Typer()


@app.command()
def grade(
    student: Annotated[
        Student,
        typer.Argument(
            parser=Student.parser,
            help="The student to assign the grade to.",
        ),
    ] = None,
    grade: int = typer.Argument(None, help="The grade value (1-6).", min=1, max=6),
    comment: str = typer.Option(
        " ", "--comment", "-c", help="Optional comment for the grade."
    ),
    number: int = typer.Option(
        0,
        "--number",
        "-n",
        help="Number of the exam, (e.g., 1 for the first exam of given type).",
    ),
    exam_type: ExamType = typer.Option(
        ExamType.MUENDLICH,
        "--exam-type",
        "-t",
        help="Type of the exam.",
    ),
    date: Annotated[
        Date,
        typer.Option(
            "--date",
            "-d",
            parser=Date.parser,
            help="Date of the grading.",
            metavar="DD-MM-YYYY",
        ),
    ] = datetime.now().strftime("%d-%m-%Y"),
    all: bool = typer.Option(
        False,
        "--all",
        "-a",
        help="Set to grade all students of this class.",
    ),
):
    """
    Add a grade for a student or all students of the class.

    Records a grade for the given student and exam type on the current or specified date,
    optionally including a --comment. Note, that --number usually should not be specified;
    it is used differentiate between exams of the same type (e.g., 1. Kurzarbeit and 2. Kurzarbeit).
    The --all option can be used to grade a whole class.
    If --all is set, all other parameters besides --exam-type are ignored
    """

    if not all and not student and not grade:
        raise typer.BadParameter(
            "If --all is not set, both student and grade must be provided."
        )

    run(student, grade, number, exam_type, date, comment, all)
