from pathlib import Path

import pandas as pd
import typer

from bell.types.cmd_args.add import Student


# TODO: lets me add student with exact same name
def run(student: Student):
    students_path = Path(".students.csv")
    if not students_path.is_file():
        typer.echo("This command must be used from within a class directory.")
        return

    df = pd.read_csv(students_path)

    if student:
        df = _add_single_student(df, student)
    else:
        df = _add_multiple_students(df)

    df.to_csv(students_path, index=False)


def _add_single_student(df: pd.DataFrame, student: Student) -> pd.DataFrame:
    new_row = {
        "first_name": student.first_name,
        "last_name": student.last_name,
    }

    if ((df == pd.Series(new_row)).all(axis=1)).any():
        typer.echo("Student already listed.")
        return df

    return pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)


def _add_multiple_students(df: pd.DataFrame) -> pd.DataFrame:
    students = []
    while True:
        user_input = input(">> ")
        if user_input == "q":
            break

        try:
            student = Student.parser(user_input)
        except typer.BadParameter as e:
            print(e)
            continue

        new_row = {
            "first_name": student.first_name,
            "last_name": student.last_name,
        }

        if ((df == pd.Series(new_row)).all(axis=1)).any():
            typer.echo("Student already listed.")
            continue

        students.append(new_row)

    return pd.concat([df, pd.DataFrame(students)], ignore_index=True)
