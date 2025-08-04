from pathlib import Path

import yaml

TEMPLATE_PATH = Path("src/bell/templates")


def run(school_name: str):
    _create_syllables_dir(school_name)
    _create_dotbell_yaml(school_name)
    _create_config_yaml(school_name)


def _create_syllables_dir(school_name: str) -> None:
    (Path(school_name) / "lehrpläne").mkdir(parents=True)


def _create_dotbell_yaml(school_name: str) -> None:
    template_path = TEMPLATE_PATH / "dotbell.yaml"
    output_path = Path(school_name) / ".bell.yaml"
    dotbell = yaml.safe_load(template_path.read_text())
    output_path.write_text(yaml.dump(dotbell, sort_keys=False))


def _create_config_yaml(school_name: str) -> None:
    template_path = TEMPLATE_PATH / "config_school.yaml"
    output_path = Path(school_name) / "config.yaml"
    config = yaml.safe_load(template_path.read_text())
    config["school_name"] = school_name
    output_path.write_text(yaml.dump(config, sort_keys=False))
