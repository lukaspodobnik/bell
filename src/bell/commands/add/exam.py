from datetime import datetime

import typer
from typing_extensions import Annotated

from bell.core.add.exam import run
from bell.types.cmd_args.add import Date
from bell.types.enums.exam_types import ExamType

app = typer.Typer()


@app.command()
def exam(
    number: int = typer.Argument(help=""),
    exam_type: ExamType = typer.Argument(help=""),
    date: Annotated[
        Date,
        typer.Option("--date", "-d", parser=Date.parser, help=""),
    ] = datetime.now().strftime("%d-%m-%Y"),
):
    run(number, exam_type, date)
