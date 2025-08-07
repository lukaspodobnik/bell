from importlib.resources import files
from pathlib import Path

import yaml

from bell.res.templates import year as year_templates
from bell.types.cmd_args.init import Year
from bell.utils.clone_files import clone_csv, clone_yaml


def run(year: Year):
    if not _bell_initialized():
        return

    year_path = _create_year_dir(year)
    _create_schedule(year_path)
    _create_config(year_path)
    _mark_as_initialized(year_path)


def _bell_initialized() -> bool:
    dotbell_path = Path(".bell.yaml")
    if not dotbell_path.is_file():
        print(".bell.yaml not found")
        return False

    dotbell = yaml.load(dotbell_path.read_text(), Loader=yaml.FullLoader)
    if not dotbell["bell_init"]:
        print("BELL not initialized")
        return False

    return True


def _create_year_dir(year: Year) -> Path:
    year_path = Path(year.value)
    year_path.mkdir()
    return year_path


def _create_schedule(year_path: Path) -> None:
    src = files(year_templates) / "schedule.csv"
    dst = year_path / "schedule.csv"
    clone_csv(src, dst)


def _create_config(year_path: Path) -> None:
    src = files(year_templates) / "config.yaml"
    dst = year_path / "config.yaml"
    clone_yaml(src, dst)


def _mark_as_initialized(year_path: Path) -> None:
    dotbell_path = Path(".bell.yaml")
    dotbell = yaml.load(dotbell_path.read_text(), Loader=yaml.FullLoader)
    dotbell[f"{year_path.name}_init"] = True
    dotbell_path.write_text(yaml.dump(dotbell))
