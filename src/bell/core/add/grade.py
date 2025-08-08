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
    print(
        f"student={student}, grade={grade}, date={date}, {assignment=}, {comment=}, {exam=}"
    )

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

    print(new_row)

    return pd.concat([df_grades, pd.DataFrame([new_row])], ignore_index=True)


def _add_multiple_grades(
    df_grades: pd.DataFrame,
    df_students: pd.DataFrame,
    date: Date,
    assignment: Assignment,
) -> pd.DataFrame:
    pass


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
