import typer
from typing_extensions import Annotated

from bell.core.remove.class_ import run
from bell.types.cmd_args.class_ import Class_
from bell.types.enums.subjects import Subject

app = typer.Typer()


@app.command("class")
def class_(
    class_name: Annotated[
        Class_,
        typer.Argument(
            parser=Class_.parser,
            help="Name of the class.",
            metavar="CLASS: e.g., 10A, 9B",
        ),
    ],
    subject: Subject = typer.Argument(help="Subject name."),
):
    """
    Remove a class from the current academic year.

    Deletes the class folder and all associated files for the specified subject.
    This command is irreversible, so use it with caution.
    """
    run(str(class_name), subject)
