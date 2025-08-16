import typer

from bell.core.remove.exam import run
from bell.types.enums.exam_types import ExamType

app = typer.Typer()


@app.command()
def exam(
    number: int = typer.Argument(
        help="Number of the exam, (e.g., 1 for the first exam of given type)."
    ),
    exam_type: ExamType = typer.Argument(help="Type of the exam."),
):
    """
    Remove a planned exam for this class.
    """
    run(number, exam_type)
