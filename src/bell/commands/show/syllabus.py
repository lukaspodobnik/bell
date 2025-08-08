import typer

from bell.core.show.syllabus import run

app = typer.Typer()


@app.command()
def syllabus():
    run()
