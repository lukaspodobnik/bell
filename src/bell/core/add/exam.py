from pathlib import Path

import pandas as pd
import typer

from bell.types.cmd_args.date import Date
from bell.types.enums.exam_types import ExamType


def run(exam_type: ExamType, date: Date):
    exams_path = Path.cwd() / ".exams.csv"
    if not exams_path.is_file():
        typer.echo("Use this command from within the classroom directory.")
        return

    df = pd.read_csv(exams_path)
    if exam_type.value in df["exam_type"].values:
        number = df.loc[df["exam_type"] == exam_type.value, "number"].max() + 1
    else:
        number = 1

    new_row = {"number": number, "exam_type": exam_type.value, "date": str(date)}

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(exams_path, index=False)
