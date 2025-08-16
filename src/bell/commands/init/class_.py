import typer
from typing_extensions import Annotated

from bell.core.init.class_ import run
from bell.types.cmd_args.class_ import Class_
from bell.types.enums.subjects import Subject

app = typer.Typer()


@app.command("class")
def class_(
    class_name: Annotated[
        Class_,
        typer.Argument(
            help="Name of the class.",
            parser=Class_.parser,
            metavar="CLASS: e.g., 10A, 9B",
        ),
    ],
    subject: Subject = typer.Argument(
        help="Subject name (e.g., maths).",
    ),
):
    """
    Initialize a class.

    Creates a directory for the specified class in the given subject within the
    current academic year. This is the third step after using 'bell init year'. Use this command
    within a year directory.
    """

    run(class_name, subject)
