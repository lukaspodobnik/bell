import typer

from . import grade, student

app = typer.Typer()

app.add_typer(grade.app)
app.add_typer(student.app)
