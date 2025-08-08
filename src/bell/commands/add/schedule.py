import typer
from typing_extensions import Annotated

from bell.core.add.schedule import run
from bell.types.cmd_args.add import Slot
from bell.types.enums.weekdays import Weekday

app = typer.Typer()


@app.command()
def schedule(
    slot: Annotated[Slot, typer.Argument(parser=Slot.parser, help="")],
    weekday: Weekday = typer.Argument(help=""),
):
    run(slot, weekday)
