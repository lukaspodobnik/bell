import typer

from bell.core.remove.exam import run
from bell.types.enums.exam_types import ExamType

app = typer.Typer()


@app.command()
def exam(
    number: int = typer.Argument(help=""), exam_type: ExamType = typer.Argument(help="")
):
    run(number, exam_type)
