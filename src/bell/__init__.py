import sys

import typer

from bell.commands.add import app as add_app
from bell.commands.init import app as init_app
from bell.commands.remove import app as remove_app
from bell.commands.show import app as show_app
from bell.utils.validation import ValidationError, validate_classroom_structure


def main() -> None:
    try:
        match " ".join(sys.argv[1:]):
            case "init":
                pass
            case "init year":
                validate_classroom_structure(year_cmd=True)
            case _:
                validate_classroom_structure()
    except ValidationError as e:
        print(f"Project structure validation failed: {e}")
        return

    app = typer.Typer()
    app.add_typer(add_app, name="add")
    app.add_typer(init_app, name="init")
    app.add_typer(remove_app, name="remove")
    app.add_typer(show_app, name="show")
    app()
