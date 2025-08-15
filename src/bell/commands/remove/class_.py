import typer
from typing_extensions import Annotated

from bell.core.remove.class_ import run
from bell.types.cmd_args.class_ import Class_
from bell.types.enums.subjects import Subject

app = typer.Typer()


@app.command("class")
def class_(
    class_name: Annotated[Class_, typer.Argument(parser=Class_.parser, help="")],
    subject: Subject = typer.Argument(help=""),
):
    run(str(class_name), subject)
