import re
from datetime import datetime

from bell.types.cmd_args import CommandArg


class Year(CommandArg):
    _error_msg = "Expected format: YYYY-YY (e.g., 2025-26)"

    def __init__(self, school_year: str):
        self._school_year = school_year

    @classmethod
    def _parse(cls, value):
        if not re.match(r"^\d{4}-\d{2}$", value):
            return None

        return Year(value)

    def __str__(self):
        return self._school_year


def current_year() -> str:
    current_year = datetime.now().year
    next_year = str((current_year + 1) % 100).zfill(2)
    return f"{current_year}-{next_year}"
