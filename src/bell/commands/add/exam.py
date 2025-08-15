from datetime import datetime

import typer
from typing_extensions import Annotated

from bell.core.add.exam import run
from bell.types.cmd_args.date import Date
from bell.types.enums.exam_types import ExamType

app = typer.Typer()


@app.command()
def exam(
    exam_type: ExamType = typer.Argument(help="Type of exam (e.g., kurzarbeit)."),
    date: Annotated[
        Date,
        typer.Option(
            "--date",
            "-d",
            parser=Date.parser,
            help="Optional date of the exam (e.g., 25-03 or 25-03-2025).",
        ),
    ] = datetime.now().strftime("%d-%m-%Y"),
):
    """
    Add a planned exam.

    Registers a new exam for the current class with the given type and optional
    date.
    """
    run(exam_type, date)
