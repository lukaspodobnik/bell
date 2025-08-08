import typer
from typing_extensions import Annotated

from bell.core.init.class_ import run
from bell.types.cmd_args.init import Class_
from bell.types.enums.subjects import Subject

app = typer.Typer()


@app.command("class")
def class_(
    class_name: Annotated[
        Class_,
        typer.Argument(
            help="Class name in ddc format", parser=Class_.parser, metavar="TEXT"
        ),
    ],
    subject: Subject = typer.Argument(
        help="Choose subject from the list to the left for this class",
    ),
):
    run(class_name, subject)
