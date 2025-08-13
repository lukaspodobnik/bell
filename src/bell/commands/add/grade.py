from datetime import datetime

import typer
from typing_extensions import Annotated

from bell.core.add.grade import run
from bell.types.cmd_args.add import Date, Grade, Student
from bell.types.enums.exam_types import ExamType

app = typer.Typer()


@app.command()
def grade(
    exam_type: ExamType = typer.Argument(help=""),
    student: Annotated[Student, typer.Argument(parser=Student.parser, help="")] = None,
    grade: Annotated[Grade, typer.Argument(parser=Grade.parser, help="")] = None,
    date: Annotated[
        Date,
        typer.Option("--date", "-d", parser=Date.parser, help=""),
    ] = datetime.now().strftime("%d-%m-%Y"),
    comment: str = typer.Option("", "--comment", "-c", help=""),
    exam: bool = typer.Option(False, "--exam", "-e", help=""),
):
    if exam and (student or grade or comment):
        raise typer.BadParameter(
            "If --exam flag is set, no other arguments and options (besides --date) must be provided."
        )

    if not exam and not student and not grade:
        raise typer.BadParameter(
            "If --exam is not set, both student and grade must be provided."
        )

    run(student, grade, date, exam_type, comment)
