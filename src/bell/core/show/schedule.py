from pathlib import Path

import pandas as pd
import typer
from rich.console import Console
from rich.table import Table


def run():
    table = Table()
    src = Path(".schedule.csv")
    for _ in range(5):
        if not src.is_file():
            src = src.parent

    if not src.is_file():
        typer.echo(
            f"Use this command from within a year directory or within one of its subdirs. You are currently in {Path.cwd()}"
        )
        return

    df = pd.read_csv(src)
    for col in df.columns:
        table.add_column(str(col))

    for row in df.itertuples(index=False):
        table.add_row(*[str(cell) for cell in row])
        table.add_section()

    Console().print(table)
