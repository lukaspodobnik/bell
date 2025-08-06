import typer

from . import grade, schedule, student

app = typer.Typer()

app.add_typer(grade.app)
app.add_typer(student.app)
app.add_typer(schedule.app)
