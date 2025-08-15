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
    student: Annotated[Student, typer.Argument(parser=Student.parser, help="")] = None,
    grade: int = typer.Argument(None, help="", min=1, max=6),
    comment: str = typer.Option(" ", "--comment", "-c", help=""),
    number: int = typer.Option(0, "--number", "-n", help=""),
    exam_type: ExamType = typer.Option(
        ExamType.MUENDLICH, "--exam-type", "-t", help=""
    ),
    date: Annotated[
        Date,
        typer.Option("--date", "-d", parser=Date.parser, help=""),
    ] = datetime.now().strftime("%d-%m-%Y"),
    all: bool = typer.Option(
        False,
        "--all",
        "-a",
        help="If set, all other parameters besides --exam-type are ignored",
    ),
):
    if not all and not student and not grade:
        raise typer.BadParameter(
            "If --all is not set, both student and grade must be provided."
        )

    run(student, grade, number, exam_type, date, comment, all)
