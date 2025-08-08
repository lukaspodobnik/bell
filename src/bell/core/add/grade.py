from pathlib import Path

import pandas as pd
import typer

from bell.types.cmd_args.add import Date, Grade, Student
from bell.types.enums.assignments import Assignment


def run(
    student: Student,
    grade: Grade,
    date: Date,
    assignment: Assignment,
    comment: str,
    exam: bool,
):
    grades_path = Path("grades.csv")
    df_grades = pd.read_csv(grades_path)
    df_students = pd.read_csv(Path("students.csv"))

    if student:
        df_grades = _add_single_grade(
            df_grades, df_students, student, grade, date, assignment, comment
        )
    else:
        df_grades = _add_multiple_grades(df_grades, df_students, date, assignment)

    df_grades.to_csv(grades_path, index=False)


def _add_single_grade(
    df_grades: pd.DataFrame,
    df_students: pd.DataFrame,
    student: Student,
    grade: Grade,
    date: Date,
    assignment: Assignment,
    comment: str,
) -> pd.DataFrame:
    student_id = _get_student_id(df_students, student)
    if not student_id:
        raise typer.BadParameter("Student does not exist.")

    new_row = {
        "student_id": student_id,
        "student_name": str(student),
        "assignment": assignment.name,
        "date": str(date),
        "grade": str(grade),
        "comment": comment,
    }

    return pd.concat([df_grades, pd.DataFrame([new_row])], ignore_index=True)


def _add_multiple_grades(
    df_grades: pd.DataFrame,
    df_students: pd.DataFrame,
    date: Date,
    assignment: Assignment,
) -> pd.DataFrame:
    row_template = {
        "student_id": None,
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
        user_input = _prompt_non_empty(student)
        if user_input == "q":
            break

        parts = user_input.strip().split(maxsplit=1)

        new_row = row_template.copy()
        new_row["student_id"] = _get_student_id(df_students, student)
        new_row["student_name"] = str(student)
        new_row["grade"] = str(Grade.parser(parts[0]))
        new_row["comment"] = parts[1] if len(parts) == 2 else ""

        grades.append(new_row)

    return pd.concat([df_grades, pd.DataFrame(grades)], ignore_index=True)


# TODO: FutureWarning? wtf, needs some sort of fix.
# Also make this case insensitive (does not work like so :/).
# Also, right now, this might yield wrong id, if two students have the exact same name.
def _get_student_id(df_students: pd.DataFrame, student: Student) -> int:
    first_name, last_name = student.first_name, student.last_name
    first_names = df_students["first_name"].values
    last_names = df_students["last_name"].values

    if not (first_name in first_names and last_name in last_names):
        return 0

    id = df_students[
        (df_students["first_name"].str.lower() == first_name.lower())
        & (df_students["last_name"].str.lower() == last_name.lower())
    ]["id"]

    return int(id)


def _prompt_non_empty(student: Student) -> str:
    while True:
        user_input = input(f">> Student: {student}\n>> ")
        if user_input:
            return user_input
