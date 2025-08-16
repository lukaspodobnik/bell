import typer

from . import class_, exam, grade, lesson, student

app = typer.Typer()

app.add_typer(class_.app)
app.add_typer(exam.app)
app.add_typer(grade.app)
app.add_typer(lesson.app)
app.add_typer(student.app)
