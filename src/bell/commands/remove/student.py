import typer
from typing_extensions import Annotated

from bell.core.remove.student import run
from bell.types.cmd_args.add import Student

app = typer.Typer()


@app.command()
def student(
    student: Annotated[Student, typer.Argument(parser=Student.parser, help="")],
) -> None:
    run(student)
