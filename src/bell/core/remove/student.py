from pathlib import Path

import pandas as pd
import typer

from bell.types.cmd_args.add import Student


def run(student: Student) -> None:
    students_path = Path.cwd() / ".students.csv"
    if not students_path.is_file():
        typer.echo(
            "Use this command from within a classroom directory (e.g. within maths/10A)"
        )
        return

    df = pd.read_csv(students_path)
    if df[
        (df["first_name"] == student.first_name)
        & (df["last_name"] == student.last_name)
    ].empty:
        typer.echo(f"Student {student} does not exist.")
        return

    df = df.drop(
        df[
            (df["first_name"] == student.first_name)
            & (df["last_name"] == student.last_name)
        ].index
    )

    df.to_csv(students_path, index=False)
