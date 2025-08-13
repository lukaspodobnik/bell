import typer

from bell.core.remove.student import run
from bell.types.cmd_args.add import Student

app = typer.Typer()


@app.command()
def student(student: Student = typer.Argument(help="")) -> None:
    run(student)
