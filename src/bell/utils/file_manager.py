from pathlib import Path

import pandas as pd


def clone_csv(src: Path, dst: Path) -> None:
    df = pd.read_csv(src)
    df.to_csv(dst, index=False)
