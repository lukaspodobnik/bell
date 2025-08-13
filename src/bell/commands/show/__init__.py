import typer

from . import grades, note, schedule, students, syllabus

app = typer.Typer()

app.add_typer(grades.app)
app.add_typer(note.app)
app.add_typer(schedule.app)
app.add_typer(students.app)
app.add_typer(syllabus.app)
