from pathlib import Path

import pandas as pd

from bell.types.cmd_args.add import Student


def run(student: Student, multiple: bool):
    print(f"student: {student}, multiple: {multiple}")

    students_path = Path("students.csv")
    df = pd.read_csv(students_path)

    if student:
        df = add_single_student(df, student)
    else:
        df = add_multiple_students(df)

    df.to_csv(students_path, index=False)


def add_single_student(df: pd.DataFrame, student: Student) -> pd.DataFrame:
    next_id = df["id"].max() + 1 if not df.empty else 1

    new_row = {
        "id": next_id,
        "first_name": student.first_name,
        "last_name": student.last_name,
    }

    return pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)


def add_multiple_students(df: pd.DataFrame) -> pd.DataFrame:
    pass
