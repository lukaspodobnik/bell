import typer
from typing_extensions import Annotated

from bell.core.show.grades import run
from bell.types.cmd_args.add import Student
from bell.types.enums.exam_types import ExamType

app = typer.Typer()


@app.command()
def grades(
    student: Annotated[
        Student, typer.Option("--student", "-s", parser=Student.parser, help="")
    ] = None,
    exam_type: ExamType = typer.Option(None, "--exam-type", "-t", help=""),
    last: bool = typer.Option(False, "--last", "-l", help=""),
):
    if (
        (student and (exam_type or last))
        or (exam_type and (student or last))
        or (last and (student or exam_type))
    ):
        raise typer.BadParameter(
            "Please provide only one of the options: --student, --exam-type, --last."
        )

    run(student, exam_type, last)
