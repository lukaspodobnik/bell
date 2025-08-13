import typer

from bell.core.show.note import run

app = typer.Typer()


@app.command()
def note(
    all: bool = typer.Option(False, "--all", "-a", help="Show all notes"),
    last_n: int = typer.Option(1, "--last-n", "-n", help="Show last N notes", min=1),
) -> None:
    run(all, last_n)
