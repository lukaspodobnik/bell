from pathlib import Path

import pandas as pd
import typer

from bell.types.cmd_args.add import Date, Grade, Student
from bell.types.enums.exam_types import ExamType


def run(
    student: Student,
    grade: Grade,
    date: Date,
    assignment: ExamType,
    comment: str,
):
    grades_path = Path(".grades.csv")
    if not grades_path.is_file():
        typer.echo("This command must be used from within a class directory.")
        return

    df_grades = pd.read_csv(grades_path)
    df_students = pd.read_csv(Path(".students.csv"))

    if student:
        df_grades = add_single_grade(
            df_grades, df_students, student, grade, date, assignment, comment
        )
    else:
        df_grades = add_multiple_grades(df_grades, df_students, date, assignment)

    df_grades.to_csv(grades_path, index=False)


def add_single_grade(
    df_grades: pd.DataFrame,
    df_students: pd.DataFrame,
    student: Student,
    grade: Grade,
    date: Date,
    assignment: ExamType,
    comment: str,
) -> pd.DataFrame:
    new_row = {
        "student_name": str(student),
        "assignment": assignment.name,
        "date": str(date),
        "grade": str(grade),
        "comment": comment,
    }

    if not (
        (
            df_students
            == pd.Series(
                {"first_name": student.first_name, "last_name": student.last_name}
            )
        ).all(axis=1)
    ).any():
        typer.echo(f"Student {student} does not exist.")
        return df_grades

    return pd.concat([df_grades, pd.DataFrame([new_row])], ignore_index=True)


def add_multiple_grades(
    df_grades: pd.DataFrame,
    df_students: pd.DataFrame,
    date: Date,
    assignment: ExamType,
) -> pd.DataFrame:
    row_template = {
        "student_name": None,
        "assignment": assignment.name,
        "date": str(date),
        "grade": None,
        "comment": "",
    }

    students = [
        Student(first, last)
        for first, last in zip(
            df_students["first_name"].values, df_students["last_name"].values
        )
    ]

    grades = []

    for student in students:
        user_input = prompt_non_empty(student)
        if user_input == "q":
            break

        parts = user_input.strip().split(maxsplit=1)

        new_row = row_template.copy()
        new_row["student_name"] = str(student)
        new_row["grade"] = str(Grade.parser(parts[0]))
        new_row["comment"] = parts[1] if len(parts) == 2 else ""

        grades.append(new_row)

    return pd.concat([df_grades, pd.DataFrame(grades)], ignore_index=True)


def prompt_non_empty(student: Student) -> str:
    while True:
        user_input = input(f">> Student: {student}\n>> ")
        if user_input:
            return user_input
