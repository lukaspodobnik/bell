import typer
from typing_extensions import Annotated

from bell.core.init import class_ as class_core
from bell.core.init import school as school_core
from bell.core.init import year as year_core
from bell.types.cmd_args.init import Year, parse_year

app = typer.Typer()


@app.command()
def school(school_name: str):
    school_core.run(school_name)


@app.command()
def year(
    year: Annotated[
        Year,
        typer.Argument(
            help="School year in YYYY-YY format", parser=parse_year, metavar="TEXT"
        ),
    ],
):
    year_core.run(year)


@app.command("class")
def class_():
    class_core.run()
