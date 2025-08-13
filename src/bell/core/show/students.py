from pathlib import Path

import pandas as pd
import typer
from rich.console import Console
from rich.table import Table


def run():
    students_path = Path(".students.csv")
    if not students_path.is_file():
        typer.echo("Use this command withing a classroom directory.")
        return

    df = pd.read_csv(students_path)
    if df.empty:
        typer.echo("No students found.")
        return

    table = Table()
    df = df.sort_values(by=["last_name", "first_name"])
    table.add_column("#", justify="right")
    for col in df.columns:
        table.add_column(str(col))

    for i, row in enumerate(df.itertuples(index=False), start=1):
        table.add_row(str(i), *[str(cell) for cell in row])
        table.add_section()

    Console().print(table)
