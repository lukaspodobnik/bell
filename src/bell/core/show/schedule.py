from pathlib import Path

import pandas as pd
import typer
from rich.console import Console
from rich.table import Table


def run():
    table = Table()
    src = Path("schedule.csv")
    if not src.is_file():
        src = Path("..") / src

    if not src.is_file():
        src = Path("..") / src

    if not src.is_file():
        typer.echo("No schedule was found.")

    df = pd.read_csv(src)
    for col in df.columns:
        table.add_column(str(col))

    for row in df.itertuples(index=False):
        table.add_row(*[str(cell) for cell in row])
        table.add_section()

    Console().print(table)
