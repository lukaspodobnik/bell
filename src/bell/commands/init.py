import typer

app = typer.Typer()


@app.command()
def school():
    print("school cmd :)")


@app.command()
def year():
    print("year cmd :))")


@app.command("class")
def class_():
    print("class cmd :)))")
