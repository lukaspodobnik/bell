from pathlib import Path

import pandas as pd
import typer
from rich.console import Console
from rich.table import Table


def run():
    exams_path = Path(".exams.csv")
    if not exams_path.is_file():
        typer.echo("Use this command from within a classroom directory.")
        return

    df = pd.read_csv(exams_path)

    table = Table()
    for col in ["#", "type", "date"]:
        table.add_column(col)

    for row in df.itertuples(index=False):
        table.add_row(*[str(cell) for cell in row])
        table.add_section()

    Console().print(table)
