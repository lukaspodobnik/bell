from datetime import datetime

import typer
from typing_extensions import Annotated

from bell.core.init.year import run
from bell.types.cmd_args.year import Year

app = typer.Typer()


@app.command()
def year(
    year: Annotated[
        Year,
        typer.Option(
            help="School year in YYYY-YY format", parser=Year.parser, metavar="TEXT"
        ),
    ] = None,
):
    if not year:
        current_year = datetime.now().year
        next_year = str((current_year + 1) % 100).zfill(2)
        year = Year(f"{current_year}-{next_year}")

    run(year)
