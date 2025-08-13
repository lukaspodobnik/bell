from pathlib import Path

import pandas as pd
import typer

from bell.types.enums.exam_types import ExamType


def run(number: int, exam_type: ExamType):
    exams_path = Path.cwd() / ".exams.csv"
    if not exams_path.is_file():
        typer.echo("Use this command from within the classroom directory.")
        return

    df = pd.read_csv(exams_path)

    if df[(df["exam_type"] == exam_type.value) & (df["number"] == number)].empty:
        typer.echo(f"No exam found with type {exam_type.value} and number {number}.")
        return

    df = df.drop(
        df[(df["exam_type"] == exam_type.value) & (df["number"] == number)].index
    )
    df.to_csv(exams_path, index=False)
