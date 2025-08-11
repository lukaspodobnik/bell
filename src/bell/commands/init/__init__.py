import typer

from bell.core.init import run

from . import class_, year

app = typer.Typer(invoke_without_command=True)

app.add_typer(year.app)
app.add_typer(class_.app)


@app.callback()
def init_callback(ctx: typer.Context):
    if ctx.invoked_subcommand:
        return

    run()
