from pathlib import Path

import pandas as pd
import typer

from bell.types.cmd_args.student import Student


def run(student: Student):
    students_path = Path(".students.csv")
    if not students_path.is_file():
        typer.echo("This command must be used from within a class directory.")
        return

    df = pd.read_csv(students_path)

    if student:
        df = add_single_student(df, student)
    else:
        df = add_multiple_students(df)

    df.to_csv(students_path, index=False)


def add_single_student(df: pd.DataFrame, student: Student) -> pd.DataFrame:
    new_row = {
        "first_name": student.first_name,
        "last_name": student.last_name,
    }

    if ((df == pd.Series(new_row)).all(axis=1)).any():
        typer.echo("Student already listed.")
        return df

    return pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)


def add_multiple_students(df: pd.DataFrame) -> pd.DataFrame:
    students: set[Student] = set()
    while True:
        user_input = input(">> ")
        if user_input == "q":
            break

        try:
            student = Student.parser(user_input)
        except typer.BadParameter as e:
            typer.echo(e)
            continue

        students.add(student)

    rows = list(
        map(
            lambda student: {
                "first_name": student.first_name,
                "last_name": student.last_name,
            },
            students,
        )
    )
    duplicates = [row for row in rows if ((df == pd.Series(row)).all(axis=1)).any()]
    if len(duplicates) > 0:
        typer.echo(
            f"These students are already listed: {list(map(lambda row: Student.parser(f'{row["first_name"]} {row["last_name"]}'), duplicates))}."
        )

    rows = [row for row in rows if row not in duplicates]

    return pd.concat([df, pd.DataFrame(rows)], ignore_index=True)
