import re
import sys
from pathlib import Path

import pdfplumber


def _get_text_from_pdf_without_headers_and_footnotes(path: Path):
    text_parts = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            width = page.width
            height = page.height
            cropped = page.crop((0, 80, width, height - 80))
            text_parts.append(cropped.extract_text())

    return "\n".join(text_parts)


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

    for _ in range(5):
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
    text = text.strip("\n")
    text = text.strip()
    path.write_text(text)


# Does not convert the math symbols :/ edit by hand...
def _convert_math_syllabus():
    dir_path = Path("src/bell/res/syllabi/maths")
    text = _get_text_from_pdf_without_headers_and_footnotes(
        dir_path / (sys.argv[2] + ".pdf")
    )

    text = text.replace("Fachlehrpläne", "")
    text = text.replace("Gymnasium:", "\n# Gymnasium:")
    text = re.sub(r"(M\d{1,2} \d{1}:)", "\n## \\1", text)
    text = re.sub(r"(M\d{1,2} \d{1}.\d{1})", "\n### \\1", text)
    text = text.replace(
        "Kompetenzerwartungen und Inhalte",
        "\n\n**Kompetenzerwartungen und Inhalte**\n\n",
    )
    text = re.sub(
        r"(?<!\*\*)Kompetenzerwartungen", "\n\n**Kompetenzerwartungen**\n\n", text
    )
    text = text.replace("Die Schülerinnen und Schüler ...", "Die Schüler ...\n")
    text = text.replace("•", "-")
    text = re.sub(r"\n{2,}", "\n\n", text)

    for _ in range(5):
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
    text = text.strip("\n")
    text = text.strip()

    # print(text)
    (dir_path / (sys.argv[2] + ".md")).write_text(text)


match sys.argv[1]:
    case "inf":
        _convert_inf_syllabus()
    case "math":
        _convert_math_syllabus()
    case _:
        print("No such subject")
