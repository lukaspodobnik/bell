from pathlib import Path

import pandas as pd
import yaml


def clone_csv(src: Path, dst: Path) -> None:
    df = pd.read_csv(src)
    df.to_csv(dst, index=False)


def clone_yaml(src: Path, dst: Path) -> None:
    src_content = src.read_text()
    src_content = yaml.load(src_content, Loader=yaml.FullLoader)
    dst_content = yaml.dump(src_content, sort_keys=False)
    dst.write_text(dst_content)
