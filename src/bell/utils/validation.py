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


def find_bell_dir(max_levels: int = 7) -> Path:
    current = Path.cwd()
    for _ in range(max_levels):
        if (current / ".bell").is_dir():
            return current
        if current.parent == current:
            break
        current = current.parent

    raise ValidationError(".bell directory not found in parent directories.")


def load_classroom_structure(
    year: str, max_levels: int = 7, bell_root: Path = None
) -> dict:
    bell_root = bell_root if bell_root else find_bell_dir(max_levels)
    yaml_path = bell_root / ".bell" / "classroom_structure" / f"{year}.yaml"
    if not yaml_path.exists():
        raise ValidationError(f"Expected structure file not found: {yaml_path}")

    return yaml.safe_load(yaml_path.read_text())


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
    bell_root = find_bell_dir(max_levels)
    if year_cmd and not (bell_root / "classroom_structure").is_dir():
        raise ValidationError(
            f"Expected sturcture directory not found: {(bell_root / 'classroom_structure')}"
        )

    expected = load_classroom_structure(find_year(max_levels), max_levels, bell_root)
    validate_structure(expected, bell_root)
