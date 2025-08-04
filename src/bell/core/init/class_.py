from pathlib import Path

import yaml

from bell.types.cmd_args.init import Class_
from bell.types.enums.subjects import Subject


def run(class_name: Class_, subject: Subject):
    if not _year_initialized():
        return

    _create_official_syllabi()
    _create_class_syllabus()
    _create_notes_dir()
    _create_students_csv()
    _create_grades_csv()
    _mark_as_initialized()


def _year_initialized() -> bool:
    dotbell_path = Path("..") / Path(".bell.yaml")
    if not dotbell_path.is_file():
        print(".bell.yaml not found")
        return False

    dotbell = yaml.load(dotbell_path.read_text())
    if dotbell.get(f"{Path('.').resolve().name}_init", None) is None:
        print("Year not initialized")
        return False

    return True


def _create_official_syllabi() -> None:
    pass


def _create_class_syllabus() -> None:
    pass


def _create_notes_dir() -> None:
    pass


def _create_students_csv() -> None:
    pass


def _create_grades_csv() -> None:
    pass


def _mark_as_initialized() -> None:
    pass
