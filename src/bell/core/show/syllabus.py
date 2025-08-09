from importlib.resources import files
from pathlib import Path

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from bell.res.syllabi import computer_science, maths
from bell.types.enums.subjects import Subject


# TODO: pick appropriate colors
def run(subject: Subject, level: int):
    if not subject:
        subject, level = _get_subject_and_level()

    match subject:
        case Subject.MATHS:
            src = files(maths)
        case Subject.COMPUTER_SCIENCE:
            src = files(computer_science)

    src /= f"{level:02}.md"
    md = Markdown(src.read_text())
    panel = Panel(md)
    Console().print(panel)


def _get_subject_and_level():
    class_path = Path(".").resolve()
    level = class_path.name[:-1]
    subject = Subject(class_path.parent.name)
    return subject, int(level)
