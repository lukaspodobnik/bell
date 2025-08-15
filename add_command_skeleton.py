import sys
from pathlib import Path

if len(sys.argv) < 3:
    print("Usage: add_command_skeleton.py <group> <command>")
    sys.exit(1)

group, command = sys.argv[1:]

src_path = Path("src") / "bell"
command_path = src_path / "commands" / group / f"{command}.py"
core_path = src_path / "core" / group / f"{command}.py"

command_content = """
import typer
from bell.core.{group}.{command} import run

app = typer.Typer()

app.command()
def {command}():
    run()
"""

core_content = """
def run():
    pass
"""

command_path.parent.mkdir(parents=True, exist_ok=True)
command_path.write_text(command_content.format(group=group, command=command))

core_path.parent.mkdir(parents=True, exist_ok=True)
core_path.write_text(core_content)

print("Do not forget to hook up the commands in the __init__.py files!")
