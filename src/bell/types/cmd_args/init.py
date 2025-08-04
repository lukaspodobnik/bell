import re

import typer


class Year:
    def __init__(self, value: str):
        if not re.match(r"^\d{4}-\d{2}$", value):
            raise typer.BadParameter("Expected format: YYYY-YY (e.g., 2025-26)")
        self.value = value

    def __str__(self):
        return self.value


def parse_year(value: str):
    return Year(value)
