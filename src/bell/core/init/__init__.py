from pathlib import Path

import typer


def run():
    try:
        Path("classroom").mkdir()
        Path(".bell/classroom_structure").mkdir(parents=True)
    except FileExistsError:
        typer.echo("bell already initialized.")
