from datetime import datetime
from importlib.resources import files
from pathlib import Path

import yaml

from bell.res import templates
from bell.types.cmd_args.init import Year


def run(year: Year):
    if not _school_initialized():
        return

    year_path = _create_year_dir(year)
    _create_callendar_dir(year_path)
    _create_config_yaml(year_path)
    _create_overview_md(year_path)


def _school_initialized():
    DOTBELL_PATH = Path(".bell.yaml")
    if not DOTBELL_PATH.is_file():
        print("School not yet initialized.")
        return False

    dotbell = yaml.safe_load(DOTBELL_PATH.read_text())
    if not dotbell["initialized"]:
        print("School not yet initialized.")
        return False

    return True


def _create_year_dir(year: Year):
    if year is None:
        current_year = datetime.now().year
        next_year = str((current_year + 1) % 100).zfill(2)
        year_path = Path(f"{current_year}-{next_year}")
    else:
        year_path = Path(year.value)

    year_path.mkdir()
    return year_path


def _create_callendar_dir(year_path: Path):
    (year_path / "kalender").mkdir()


def _create_config_yaml(year_path: Path):
    config = yaml.safe_load((files(templates) / "config_year.yaml").read_text())
    (year_path / "config.yaml").write_text(yaml.dump(config, sort_keys=False))


def _create_overview_md(year_path: Path):
    overview = (files(templates) / "year_overview.md").read_text(encoding="utf-8")
    overview = overview.replace("{{ year }}", year_path.__str__())
    (year_path / "overview.md").write_text(overview, encoding="utf-8")
