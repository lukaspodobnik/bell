import typer

from bell.core.init import run

from . import class_, year

app = typer.Typer(invoke_without_command=True)

app.add_typer(year.app)
app.add_typer(class_.app)


@app.callback()
def init_callback(
    ctx: typer.Context,
    root_name: str = typer.Option(
        "classroom", "--name", "-n", help="Name your root directory"
    ),
):
    if ctx.invoked_subcommand:
        return

    run(root_name)
