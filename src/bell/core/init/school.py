from importlib.resources import files
from pathlib import Path

import yaml

from bell import templates


def run(school_name: str):
    _create_syllables_dir(school_name)
    _create_dotbell_yaml(school_name)
    _create_config_yaml(school_name)


def _create_syllables_dir(school_name: str) -> None:
    (Path(school_name) / "lehrpläne").mkdir(parents=True)


def _create_dotbell_yaml(school_name: str) -> None:
    dotbell = yaml.safe_load((files(templates) / "dotbell.yaml").read_text())
    (Path(school_name) / ".bell.yaml").write_text(yaml.dump(dotbell, sort_keys=False))


def _create_config_yaml(school_name: str) -> None:
    config = yaml.safe_load((files(templates) / "config_school.yaml").read_text())
    config["school_name"] = school_name
    (Path(school_name) / "config.yaml").write_text(yaml.dump(config, sort_keys=False))
