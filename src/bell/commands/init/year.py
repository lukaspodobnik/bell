import typer
from typing_extensions import Annotated

from bell.core.init.year import run
from bell.types.cmd_args.init import Year, parse_year

app = typer.Typer()


@app.command()
def year(
    year: Annotated[
        Year,
        typer.Option(
            help="School year in YYYY-YY format", parser=parse_year, metavar="TEXT"
        ),
    ] = None,
):
    run(year)
