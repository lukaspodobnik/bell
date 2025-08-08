from pathlib import Path

import pandas as pd
import typer

from bell.types.cmd_args.add import Student


# TODO: lets me add student with exact same name
def run(student: Student):
    students_path = Path("students.csv")
    df = pd.read_csv(students_path)

    if student:
        df = _add_single_student(df, student)
    else:
        df = _add_multiple_students(df)

    df.to_csv(students_path, index=False)


def _add_single_student(df: pd.DataFrame, student: Student) -> pd.DataFrame:
    new_row = {
        "id": _get_next_id(df),
        "first_name": student.first_name,
        "last_name": student.last_name,
    }

    return pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)


def _add_multiple_students(df: pd.DataFrame) -> pd.DataFrame:
    students = []
    next_id = _get_next_id(df)
    while True:
        user_input = input(">> ")
        if user_input == "q":
            break

        try:
            student = Student.parser(user_input)
        except typer.BadParameter as e:
            print(e)
            continue

        students.append(
            {
                "id": next_id,
                "first_name": student.first_name,
                "last_name": student.last_name,
            }
        )

        next_id += 1

    return pd.concat([df, pd.DataFrame(students)], ignore_index=True)


def _get_next_id(df: pd.DataFrame):
    return df["id"].max() + 1 if not df.empty else 1
