from importlib.resources import files
from pathlib import Path

import typer
import yaml

from bell.res.templates import class_ as class_templates
from bell.types.cmd_args.init import Class_
from bell.types.enums.subjects import Subject
from bell.utils.file_manager import clone_csv


def run(class_: Class_, subject: Subject):
    class_path = Path(subject.value) / str(class_)
    try:
        create_class_dir(class_path)
    except FileExistsError:
        typer.echo("Class already initialized.")

    create_notes_dir(class_path)
    create_students_csv(class_path)
    create_grades_csv(class_path)

    crs_path = Path("..") / ".bell" / "classroom_structure" / Path.cwd().name / ".yaml"
    crs = yaml.safe_load(crs_path.read_text())
    crs[subject.value] = {
        str(class_): {".notes": {}, ".students.csv": None, ".grades.csv": None},
    }
    crs_path.write_text(yaml.dump(crs))


def create_class_dir(class_path: Path) -> None:
    class_path.parent.mkdir(exist_ok=True)
    class_path.mkdir()


def create_notes_dir(class_path: Path) -> None:
    (class_path / ".notes").mkdir()


def create_students_csv(class_path: Path) -> None:
    src = files(class_templates) / "students.csv"
    dst = class_path / ".students.csv"
    clone_csv(src, dst)


def create_grades_csv(class_path: Path) -> None:
    src = files(class_templates) / "grades.csv"
    dst = class_path / ".grades.csv"
    clone_csv(src, dst)
