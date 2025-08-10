import re
import sys
from pathlib import Path


def _convert_inf_syllabus():
    path = Path("src/bell/res/syllabi/computer_science") / (sys.argv[2] + ".md")
    text = path.read_text()

    text = text.replace("Gymnasium:", "\n# Gymnasium:")
    text = re.sub(r"Inf\d{1,2}", "\n##", text)
    text = text.replace("Kompetenzerwartungen", "\n\n**Kompetenzerwartungen**\n\n")
    text = text.replace(
        "Inhalte zu den Kompetenzen:", "\n\n**Inhalte zu den Kompetenzen:**\n\n"
    )
    text = text.replace("Die Schülerinnen und Schüler ...", "Die Schüler ...\n")
    text = text.replace("•", "-")
    text = re.sub(r"\n{2,}", "\n\n", text)

    for _ in range(3):
        lines = text.split("\n")
        text = ""
        jump = False
        for i, line in enumerate(lines):
            if jump:
                jump = False
                continue
            if line.startswith("-"):
                if not lines[i + 1].startswith("-") and lines[i + 1] != "":
                    line += " " + lines[i + 1]
                    jump = True

            text += line + "\n"

    text = re.sub(r" {2,}", " ", text)
    path.write_text(text.strip("\n"))


def _convert_math_syllabus():
    pass


match sys.argv[1]:
    case "inf":
        _convert_inf_syllabus()
    case "math":
        _convert_math_syllabus()
    case _:
        print("No such subject")
