import typer

from . import schedule, syllabus

app = typer.Typer()

app.add_typer(schedule.app)
app.add_typer(syllabus.app)
