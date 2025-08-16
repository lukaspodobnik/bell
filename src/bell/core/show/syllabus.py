import re
from importlib.resources import files
from pathlib import Path

import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from bell.res.syllabi import computer_science, maths
from bell.types.enums.class_types import ClassType
from bell.types.enums.subjects import Subject


def run(subject: Subject, grade_level: int, class_type: ClassType):
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

    match class_type:
        case ClassType.NORMAL:
            src /= f"{grade_level:02}.md"
        case ClassType.VERTIEFUNG:
            src /= f"{grade_level:02}_vertiefung.md"
        case ClassType.SPAET_BEGINNEND:
            src /= f"{grade_level:02}_spaet_beginnend.md"
        case ClassType.ERHOEHTES_NIVEAU:
            src /= f"{grade_level:02}_erhoehtes_niveau.md"

    if not src.is_file():
        typer.echo("The specified syllabus does not exist.")
        return

    md = Markdown(src.read_text())
    panel = Panel(md)
    Console().print(panel)
