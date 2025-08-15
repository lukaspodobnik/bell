from pathlib import Path

import pandas as pd
import typer
from rich.console import Console
from rich.table import Table

from bell.types.cmd_args.add import Student
from bell.types.enums.exam_types import ExamType


def run(student: Student, exam_type: ExamType, last: bool) -> None:
    grades_path = Path(".grades.csv")
    if not grades_path.is_file():
        typer.echo("Use this command from within a class directory.")
        return

    df_grades = pd.read_csv(grades_path)

    if student:
        df_students = pd.read_csv(Path(".students.csv"))
        if df_students[
            (df_students["first_name"] == student.first_name)
            & (df_students["last_name"] == student.last_name)
        ].empty:
            typer.echo(f"{student} not found.")
            return

        if df_grades[(df_grades["student_name"] == str(student))].empty:
            typer.echo(f"{student} has no grades.")
            return

        table = create_grades_table_for_student(df_grades, student)

    elif exam_type:
        if df_grades[(df_grades["exam_type"] == exam_type.value)].empty:
            typer.echo(f"No grades found for exam type {exam_type.value}.")
            return

        table = create_grades_table_for_exam_type(df_grades, exam_type)

    elif last:
        if df_grades[(df_grades["exam_type"] != "mündlich")].empty:
            typer.echo("No graded exam found.")
            return

        table = create_grades_table_for_last_exam(df_grades)

    else:
        if df_grades.empty:
            typer.echo("No grades found.")
            return

        table = create_grades_table_for_all_grades(df_grades)

    Console().print(table)


def create_grades_table_for_student(df: pd.DataFrame, student: Student) -> Table:
    table = Table(title=f"Grades for {student}")
    for col in ["#", "type", "date", "grade", "comment"]:
        table.add_column(col)

    df = (
        df[df["student_name"] == str(student)]
        .drop(columns=["student_name"])
        .sort_values(by=["exam_type", "number"])
    )

    next_type = True
    for row in df.itertuples(index=False):
        if next_type:
            last_exam_type = row.exam_type
            next_type = False

        if row.exam_type != last_exam_type:
            table.add_section()
            last_exam_type = row.exam_type
            next_type = True

        table.add_row(*[str(cell) for cell in row])

    return table


def create_grades_table_for_exam_type(df: pd.DataFrame, exam_type: ExamType) -> Table:
    table = Table()
    for col in ["#", "type", "date", "name", "grade", "comment"]:
        table.add_column(col)

    df = df[df["exam_type"] == exam_type.value].sort_values(
        by=["number", "student_name"]
    )

    new_number = True
    for row in df.itertuples(index=False):
        if new_number:
            last_number = row.number
            new_number = False

        if row.number != last_number:
            table.add_section()
            last_number = row.number
            new_number = True

        table.add_row(
            str(row.number),
            str(row.exam_type),
            str(row.date),
            str(row.student_name),
            str(row.grade),
            str(row.comment),
        )

    return table


def create_grades_table_for_last_exam(df: pd.DataFrame) -> Table:
    table = Table()
    for col in ["#", "type", "date", "name", "grade", "comment"]:
        table.add_column(col)

    latest = pd.to_datetime(df["date"], format="%d-%m-%Y").max().strftime("%d-%m-%Y")
    df = df[(df["exam_type"] != "mündlich") & (df["date"] == latest)].sort_values(
        by=["student_name"]
    )

    for row in df.itertuples(index=False):
        table.add_row(
            str(row.number),
            str(row.exam_type),
            str(row.date),
            str(row.student_name),
            str(row.grade),
            str(row.comment),
        )

    return table


def create_grades_table_for_all_grades(df: pd.DataFrame) -> Table:
    table = Table()
    for col in ["#", "type", "date", "name", "grade", "comment"]:
        table.add_column(col)

    df = df.sort_values(by=["exam_type", "number", "student_name"])

    new_number = True
    new_type = True
    for row in df.itertuples(index=False):
        if new_number:
            last_number = row.number
            new_number = False

        if new_type:
            last_exam_type = row.exam_type
            new_type = False

        if row.number != last_number:
            table.add_section()
            last_number = row.number
            new_number = True

        if row.exam_type != last_exam_type:
            table.add_section()
            last_exam_type = row.exam_type
            new_type = True

        table.add_row(
            str(row.number),
            str(row.exam_type),
            str(row.date),
            str(row.student_name),
            str(row.grade),
            str(row.comment),
        )

    return table
