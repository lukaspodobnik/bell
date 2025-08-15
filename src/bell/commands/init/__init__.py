import typer

from bell.core.init import run

from . import class_, year

app = typer.Typer(invoke_without_command=True)

app.add_typer(year.app)
app.add_typer(class_.app)


@app.callback()
def init_callback(ctx: typer.Context):
    """
    Initialize a new classroom workspace.

    Sets up the main classroom directory in the current directory. This is the first
    step for using BELL and must be run before initializing years or classes.
    """
    if ctx.invoked_subcommand:
        return

    run()
