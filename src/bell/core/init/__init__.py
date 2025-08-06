from importlib.resources import files
from pathlib import Path

from bell.res.templates import root as root_templates
from bell.utils.clone_files import clone_yaml


def run(root_name: str):
    _create_root_dir(root_name)
    _create_config(root_name)
    _create_dotbell(root_name)


def _create_root_dir(root_name: str) -> None:
    Path(root_name).mkdir()


def _create_config(root_name: str) -> None:
    src = files(root_templates) / "config.yaml"
    dst = Path(root_name) / "config.yaml"
    clone_yaml(src, dst)


def _create_dotbell(root_name: str) -> None:
    src = files(root_templates) / "dotbell.yaml"
    dst = Path(root_name) / ".bell.yaml"
    clone_yaml(src, dst)
