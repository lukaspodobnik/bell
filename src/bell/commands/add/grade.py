from datetime import datetime

import typer
from typing_extensions import Annotated

from bell.core.add.grade import run
from bell.types.cmd_args.add import Date, Grade, Student
from bell.types.enums.assignments import Assignment

app = typer.Typer()


@app.command()
def grade(
    student: Annotated[Student, typer.Argument(parser=Student.parser, help="")] = None,
    grade: Annotated[Grade, typer.Argument(parser=Grade.parser, help="")] = None,
    date: Annotated[
        Date,
        typer.Option("--date", "-d", parser=Date.parser, help=""),
    ] = Date.parser(datetime.now().strftime("%d-%m")),
    assignment: Assignment = typer.Option(
        Assignment.NOSPEC, "--assignment", "-a", help=""
    ),
    comment: str = typer.Option("", "--comment", "-c", help=""),
    exam: bool = typer.Option(False, "--exam", "-e", help=""),
):
    if exam and (student or grade or comment):
        raise typer.BadParameter(
            "If --exam flag is set, no other arguments and options (besides --date and --assignment) must be provided."
        )

    if not student or not grade:
        raise typer.BadParameter(
            "If --exam is not set, both student and grade must be provided."
        )

    run(student, grade, date, assignment, comment, exam)
