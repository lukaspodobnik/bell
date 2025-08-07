from datetime import datetime

import typer
from typing_extensions import Annotated

from bell.core.add.grade import run
from bell.types.cmd_args.add import Date, Grade, Student

app = typer.Typer()


@app.command()
def grade(
    student_name: Annotated[Student, typer.Argument(parser=Student.parse, help="")],
    grade: Annotated[Grade, typer.Argument(parser=Grade.parse, help="")],
    date: Annotated[
        Date,
        typer.Option(
            datetime.now().strftime("%d-%m"), "--date", "-d", parser=Date.parse, help=""
        ),
    ],
    oral: bool = typer.Option(False, "--oral", "-o", help=""),
    exam: bool = typer.Option(False, "--exam", "-e", help=""),
    comment: str = typer.Option("", "--comment", "-c", help=""),
):
    run()
