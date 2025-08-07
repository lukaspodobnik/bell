from bell.types.cmd_args.add import Slot
from bell.types.enums.weekdays import Weekday


def run(slot: Slot, weekday: Weekday):
    print(f"slot={slot}, weekday={weekday.name}")
