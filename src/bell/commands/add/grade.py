from datetime import datetime

import typer
from typing_extensions import Annotated

from bell.core.add.grade import run
from bell.types.cmd_args.add import Date, Grade, Student

app = typer.Typer()


@app.command()
def grade(
    student: Annotated[Student, typer.Argument(parser=Student.parse, help="")] = None,
    grade: Annotated[Grade, typer.Argument(parser=Grade.parse, help="")] = None,
    date: Annotated[
        Date,
        typer.Option("--date", "-d", parser=Date.parse, help=""),
    ] = datetime.now().strftime("%d-%m"),
    oral: bool = typer.Option(False, "--oral", "-o", help=""),
    comment: str = typer.Option("", "--comment", "-c", help=""),
    exam: bool = typer.Option(False, "--exam", "-e", help=""),
):
    if exam and (student or grade or oral or comment != ""):
        raise typer.BadParameter(
            "If --exam flag is set, no other arguments and options (besides --date) must be provided."
        )

    if not student or not grade:
        raise typer.BadParameter(
            "If --exam is not set, both student and grade must be provided."
        )

    run(student, grade, date, oral, comment, exam)
