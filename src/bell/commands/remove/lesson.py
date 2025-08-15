import typer

from bell.core.remove.lesson import run
from bell.types.enums.weekdays import Weekday

app = typer.Typer()


@app.command()
def lesson(
    slot: int = typer.Argument(min=1, max=6, help="Time slot of the lesson."),
    weekday: Weekday = typer.Argument(help="Weekday of the lesson."),
):
    """
    Remove a lesson from the schedule for this year.
    """
    run(slot, weekday)
