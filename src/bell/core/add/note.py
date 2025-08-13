from datetime import datetime
from pathlib import Path


def run():
    notes_path = Path.cwd() / "notes"
    if not notes_path.is_dir():
        print("Use this command in a class direcotry.")
        return

    header = input("Enter note header: ")
    if header == "q":
        return

    content = ""
    while True:
        line = input("Enter note content (or 'q' to finish): ")
        if line == "q":
            break
        content += line + "\n"

    content = content.strip()
    note = f"# {header}\n\n{content}" if header else content
    note_path = notes_path / f"{find_next_note_name(notes_path)}.md"
    note_path.write_text(note)


def find_next_note_name(path: Path) -> str:
    prefix = datetime.now().strftime("%d-%m-%y")
    max = 0
    for f in path.glob(f"{prefix}_*.md"):
        num = f.stem.split("_")[-1]
        if int(num) > max:
            max = int(num)

    return f"{prefix}_{(max + 1):02d}"
