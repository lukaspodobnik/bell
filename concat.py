import re
from pathlib import Path

priority_order = ["init", "add", "remove", "show"]


def sort_key(path: Path):
    # Extract the start of the filename (before first space/underscore/etc.)
    name = path.stem  # no file extension
    for index, prefix in enumerate(priority_order):
        if name.startswith(prefix):
            return index  # lower index = higher priority
    return len(priority_order)


directory = Path("docs")

all_text = []

for file_path in sorted(directory.iterdir(), key=sort_key):
    if file_path.is_file():
        with file_path.open("r", encoding="utf-8") as f:
            all_text.append(f.read())

# Join everything with a newline
combined_text = "\n".join(all_text)
combined_text = re.sub(r"(?m)^# (?!#)", "### ", combined_text)
combined_text = combined_text.replace("[default: 16-08-2025]", "")
combined_text = combined_text.replace("CLASS: e.g., 10A, 9B", "[CLASS]")
combined_text = combined_text.replace(
    "Name of the class.", "Name of the class, e.g., 10A or 9B"
)

(Path.cwd() / "manual.md").write_text(combined_text)
