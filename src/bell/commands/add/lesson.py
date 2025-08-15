import typer

from bell.core.add.lesson import run
from bell.types.enums.weekdays import Weekday

app = typer.Typer()


@app.command()
def lesson(
    slot: int = typer.Argument(min=1, max=6, help="Time slot of the lesson."),
    weekday: Weekday = typer.Argument(help="Weekday of the lesson."),
):
    """
    Add a lesson to the schedule.

    Assigns the current class and subject to the specified slot and weekday in
    the schedule.
    """

    run(slot, weekday)
