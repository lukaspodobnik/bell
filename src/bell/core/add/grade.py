from pathlib import Path

import pandas as pd
import typer

from bell.types.cmd_args.date import Date
from bell.types.cmd_args.student import Student
from bell.types.enums.exam_types import ExamType


def run(
    student: Student,
    grade: int,
    number: int,
    exam_type: ExamType,
    date: Date,
    comment: str,
    all: bool,
):
    grades_path = Path(".grades.csv")
    if not grades_path.is_file():
        typer.echo("This command must be used from within a class directory.")
        return

    df_grades = pd.read_csv(grades_path)
    df_students = pd.read_csv(Path(".students.csv"))

    if student:
        df_grades = add_single_grade(
            df_grades, df_students, student, grade, number, exam_type, date, comment
        )
    else:
        df_grades = add_multiple_grades(df_grades, df_students, date, exam_type)

    df_grades.to_csv(grades_path, index=False)


def add_single_grade(
    df_grades: pd.DataFrame,
    df_students: pd.DataFrame,
    student: Student,
    grade: int,
    number: int,
    exam_type: ExamType,
    date: Date,
    comment: str,
) -> pd.DataFrame:
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

    number = find_exam_number(df_grades, exam_type, student) if number == 0 else number
    new_row = {
        "student_name": str(student),
        "number": str(number),
        "exam_type": exam_type.value,
        "date": str(date),
        "grade": str(grade),
        "comment": comment,
    }

    return pd.concat([df_grades, pd.DataFrame([new_row])], ignore_index=True)


def add_multiple_grades(
    df_grades: pd.DataFrame,
    df_students: pd.DataFrame,
    date: Date,
    exam_type: ExamType,
) -> pd.DataFrame:
    row_template = {
        "exam_type": exam_type.value,
        "date": str(date),
        "comment": " ",
    }

    students = [
        Student(first, last)
        for first, last in zip(
            df_students["first_name"].values, df_students["last_name"].values
        )
    ]

    grades = []

    for student in students:
        user_input = prompt_grade(student)
        if user_input == "q":
            break

        parts = user_input.split(maxsplit=1)

        new_row = row_template.copy()
        new_row["student_name"] = str(student)
        new_row["number"] = find_exam_number(df_grades, exam_type, student)
        new_row["grade"] = str(int(parts[0]))
        new_row["comment"] = parts[1] if len(parts) == 2 else " "

        grades.append(new_row)

    return pd.concat([df_grades, pd.DataFrame(grades)], ignore_index=True)


def prompt_grade(student: Student) -> str:
    while True:
        user_input = input(f">> Student: {student}\n>> ").strip()
        if not user_input:
            continue

        if user_input != "q" and (
            not user_input.isdigit() or not (1 <= int(user_input) <= 6)
        ):
            typer.echo("Invalid grade. Please enter a number between 1 and 6.")
            continue

        return user_input


def find_exam_number(
    df_grades: pd.DataFrame, exam_type: ExamType, student: Student
) -> int:
    numbers = df_grades.loc[
        (df_grades["exam_type"] == exam_type.value)
        & (df_grades["student_name"] == str(student)),
        "number",
    ]

    return numbers.max() + 1 if not numbers.empty else 1
