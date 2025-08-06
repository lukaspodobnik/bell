from importlib.resources import files
from pathlib import Path

import yaml

from bell.res.templates import class_ as class_templates
from bell.types.cmd_args.init import Class_
from bell.types.enums.subjects import Subject
from bell.utils.clone_files import clone_csv


def run(class_: Class_, subject: Subject):
    if not _year_initialized():
        return

    class_path = _create_class_dir(class_, subject)
    _create_notes_dir(class_path)
    _create_students_csv(class_path)
    _create_grades_csv(class_path)
    _mark_as_initialized()


def _year_initialized() -> bool:
    dotbell_path = Path("..") / Path(".bell.yaml")
    if not dotbell_path.is_file():
        print(".bell.yaml not found")
        return False

    dotbell = yaml.load(dotbell_path.read_text(), Loader=yaml.FullLoader)
    if dotbell.get(f"{Path('.').resolve().name}_init", None) is None:
        print("Year not initialized")
        return False

    return True


def _create_class_dir(class_: Class_, subject: Subject) -> Path:
    class_path = subject.value / Path(class_.value)
    class_path.mkdir(parents=True, exist_ok=True)
    return class_path


def _create_notes_dir(class_path: Path) -> None:
    (class_path / "notes").mkdir()


def _create_students_csv(class_path: Path) -> None:
    src = files(class_templates) / "students.csv"
    dst = class_path / "students.csv"
    clone_csv(src, dst)


def _create_grades_csv(class_path: Path) -> None:
    src = files(class_templates) / "grades.csv"
    dst = class_path / "grades.csv"
    clone_csv(src, dst)


def _mark_as_initialized() -> None:
    pass
