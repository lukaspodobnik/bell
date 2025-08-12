import re
from pathlib import Path

import yaml


class ValidationError(Exception):
    pass


def find_year(max_levels: int = 7) -> str:
    year_pattern = re.compile(r"^\d{4}-\d{2}$")
    current = Path.cwd()
    for _ in range(max_levels):
        if year_pattern.match(current.name):
            return current.name
        if current.parent == current:
            break
        current = current.parent

    raise ValidationError("Year directory not found.")


def find_root(max_levels: int = 7) -> Path:
    current = Path.cwd()
    for _ in range(max_levels):
        if (current / ".bell").is_dir():
            return current
        if current.parent == current:
            break
        current = current.parent

    raise ValidationError("classroom directory not found.")


def load_classroom_structure(path: Path, max_levels: int = 7) -> dict:
    path = Path(str(path) + ".yaml")
    if not path.exists():
        raise ValidationError(f"Expected structure file not found: {path}")

    return yaml.safe_load(path.read_text())


def validate_structure(expected: dict, current_path: Path) -> None:
    for name, value in expected.items():
        target = current_path / name
        if isinstance(value, dict):
            if not target.is_dir():
                raise ValidationError(f"Missing directory: {target}")
            validate_structure(value, target)
        else:
            if not target.is_file():
                raise ValidationError(f"Missing file: {target}")


def validate_classroom_structure(max_levels: int = 7, year_cmd: bool = False) -> None:
    root_path = find_root(max_levels)
    crs_path = root_path / ".bell" / "classroom_structure"
    if year_cmd:
        if not (crs_path).is_dir():
            raise ValidationError(f"Expected sturcture directory not found: {crs_path}")
        return

    year = find_year(max_levels)
    if not (root_path / year).is_dir():
        raise ValidationError(f"Expected year directory not found: {root_path / year}")
    expected = load_classroom_structure(crs_path / year, max_levels)
    validate_structure(expected, root_path / year)
