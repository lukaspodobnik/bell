from pathlib import Path

import pandas as pd

from bell.types.cmd_args.add import Slot
from bell.types.enums.subjects import Subject
from bell.types.enums.weekdays import Weekday


def run(slot: Slot, weekday: Weekday):
    schedule_path = Path("..") / Path("..") / Path("schedule.csv")
    class_path = Path(".").resolve()
    df = pd.read_csv(schedule_path, index_col="Slot")

    df.at[slot.num, weekday.value.capitalize()] = (
        f"{class_path.name}-{Subject(class_path.parent.name).name}"
    )

    df.to_csv(schedule_path)
