from pathlib import Path

import pandas as pd
import typer

from bell.types.cmd_args.add import Student
from bell.types.enums.exam_types import ExamType


def run(student: Student, number: int, exam_type: ExamType) -> None:
    grades_path = Path(".grades.csv")
    if not grades_path.is_file():
        typer.echo("Use this command from within a classroom directory.")
        return

    df = pd.read_csv(grades_path)
    if df[
        (df["student_name"] == str(student))
        & (df["number"] == number)
        & (df["exam_type"] == exam_type.value)
    ].empty:
        typer.echo(f"{student} has no grade for {number}. {exam_type.value}")
        return

    df = df.drop(
        df[
            (df["student_name"] == str(student))
            & (df["number"] == number)
            & (df["exam_type"] == exam_type.value)
        ].index
    )

    df.to_csv(grades_path, index=False)
