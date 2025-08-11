from importlib.resources import files
from pathlib import Path

import typer
import yaml

from bell.res.templates import year as year_templates
from bell.types.cmd_args.init import Year
from bell.utils.file_manager import clone_csv


def run(year: Year):
    if Path.cwd().name != "classroom":
        typer.echo(
            "Use this command from within your classroom (your bell root directory)."
        )
        return

    year_path = Path(str(year))
    try:
        year_path.mkdir()
    except FileExistsError:
        typer.echo("Year already initialized.")
        return

    clone_csv(files(year_templates) / "schedule.csv", year_path / ".schedule.csv")

    # create the year yaml at .bell/classroom_structure/
    (Path(".bell") / "classroom_structure" / str(year) / ".yaml").write_text(
        yaml.dump({".schedule.csv": None})
    )
