import typer
from typing_extensions import Annotated

from bell.core.init import class_ as class_core
from bell.types.cmd_args.init import Class_, parse_class_
from bell.types.enums.subjects import Subject

app = typer.Typer()


@app.command("class")
def class_(
    class_: Annotated[
        Class_,
        typer.Argument(
            help="Class name in ddc format", parser=parse_class_, metavar="TEXT"
        ),
    ],
    subject: Subject = typer.Option(
        None,
        "--subject",
        "-s",
        help="Choose subject from the list to the left for this class",
    ),
):
    class_core.run(class_, subject)
