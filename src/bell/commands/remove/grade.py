import typer
from typing_extensions import Annotated

from bell.core.remove.grade import run
from bell.types.cmd_args.add import Student
from bell.types.enums.exam_types import ExamType

app = typer.Typer()


@app.command()
def grade(
    student: Annotated[Student, typer.Argument(parser=Student.parser, help="")],
    number: int = typer.Argument(help=""),
    exam_type: ExamType = typer.Argument(help=""),
):
    run(student, number, exam_type)
