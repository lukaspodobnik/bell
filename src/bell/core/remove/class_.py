import shutil
from pathlib import Path

import typer
import yaml

from bell.types.enums.subjects import Subject


def run(class_name: str, subject: Subject) -> None:
    year_path = Path.cwd()
    if not (year_path / ".schedule.csv").is_file():
        typer.echo("Use this command from within a year directory.")
        return

    user_input = input(
        "Are you sure you want to remove the current class? All data will be lost. Type the class-name (e.g. 10A) to confirm, or q to quit: "
    )

    if user_input.lower() == "q":
        return

    if user_input.upper() != class_name.upper():
        typer.echo("Class name does not match. Aborting.")
        return

    yaml_path = (
        year_path.parent / ".bell" / "classroom_structure" / f"{year_path.name}.yaml"
    )

    shutil.rmtree(year_path / subject.value / class_name)

    crs = yaml.safe_load(yaml_path.read_text())
    del crs[subject.value][class_name.upper()]
    yaml_path.write_text(yaml.dump(crs))

    typer.echo("Class removed successfully.")
