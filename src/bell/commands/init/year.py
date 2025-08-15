import typer
from typing_extensions import Annotated

from bell.core.init.year import run
from bell.types.cmd_args.year import Year, current_year

app = typer.Typer()


@app.command()
def year(
    year: Annotated[
        Year,
        typer.Option(
            ...,
            "--year",
            "-y",
            help="Specify a different academic year (e.g., 2024-25).",
            parser=Year.parser,
        ),
    ] = current_year(),
):
    """
    Initialize the academic year.

    Creates a directory for the current (or specified) academic year inside the
    classroom workspace. This is the second step after using 'bell init'. Use this command
    within the classroom directory.
    """

    run(year)
