from importlib.resources import files
from pathlib import Path

import yaml

from bell.res import templates


def run(root_name: str):
    _create_syllables_dir(root_name)
    _create_config_yaml(root_name)
    _create_dotbell_yaml(root_name)


def _create_syllables_dir(root_name: str) -> None:
    (Path(root_name) / "lehrpläne").mkdir(parents=True)


def _create_config_yaml(root_name: str) -> None:
    config = yaml.load((files(templates) / "config_root.yaml").read_text())
    (Path(root_name) / "config.yaml").write_text(yaml.dump(config, sort_keys=False))


def _create_dotbell_yaml(root_name: str) -> None:
    dotbell = yaml.load((files(templates) / "dotbell.yaml").read_text())
    dotbell["bell_init"] = True
    (Path(root_name) / ".bell.yaml").write_text(yaml.dump(dotbell, sort_keys=False))
