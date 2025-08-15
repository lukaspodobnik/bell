import re
from pathlib import Path

import pandas as pd
import typer

from bell.types.enums.subjects import Subject
from bell.types.enums.weekdays import Weekday


def run(slot: int, weekday: Weekday):
    class_path = Path.cwd()
    if not re.match(r"^\d{1,2}[A-Z]$", class_path.name):
        typer.echo(
            "Use this command from within a class direcotry (e. g. within maths/10A)"
        )
        return
    schedule_path = class_path.parent.parent / ".schedule.csv"

    df = pd.read_csv(schedule_path, index_col="#")
    df.at[slot, weekday.value.capitalize()] = (
        f"{class_path.name}-{Subject(class_path.parent.name).name}"
    )
    df.to_csv(schedule_path)
