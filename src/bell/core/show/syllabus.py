import re
from importlib.resources import files
from pathlib import Path

import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from bell.res.syllabi import computer_science, maths
from bell.types.enums.subjects import Subject


def run(subject: Subject, grade_level: int):
    if not subject:
        class_path = Path.cwd()
        if not re.match(r"^\d{1,2}[A-Z]$", class_path.name):
            typer.echo(
                "Use this command from within a class direcotry (e. g. within maths/10A)"
            )
            return

        subject = Subject(class_path.parent.name)
        grade_level = int(class_path.name[:-1])

    match subject:
        case Subject.MATHS:
            src = files(maths)
        case Subject.COMPUTER_SCIENCE:
            src = files(computer_science)

    src /= f"{grade_level:02}.md"
    md = Markdown(src.read_text())
    panel = Panel(md)
    Console().print(panel)
