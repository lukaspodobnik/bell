from pathlib import Path

import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel


def run(all: bool, last_n: int) -> None:
    notes_path = Path.cwd() / "notes"
    if not notes_path.is_dir():
        typer.echo(
            "Use this command form within a class directory (e.g. within maths/10A)"
        )
        return

    files = sorted(
        list(notes_path.glob("*.md")), key=lambda f: f.stat().st_mtime, reverse=True
    )
    if not files:
        typer.echo("No notes found.")
        return

    console = Console()
    files_to_show = files if all else files[:last_n]
    for file in files_to_show:
        md = Markdown(file.read_text())
        panel = Panel(md)
        console.print(panel)
