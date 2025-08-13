import typer

from . import exam, grade, lesson, student

app = typer.Typer()
app.add_typer(exam.app)
app.add_typer(grade.app)
app.add_typer(lesson.app)
app.add_typer(student.app)
