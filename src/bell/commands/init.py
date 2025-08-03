import typer

from bell.core import class__, school_, year_

app = typer.Typer()


@app.command()
def school():
    school_.run()


@app.command()
def year():
    year_.run()


@app.command("class")
def class_():
    class__.run()
