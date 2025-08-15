import re
from datetime import datetime

from bell.types.cmd_args import CommandArg


class Date(CommandArg):
    _error_msg = "Expected format: DD-MM or DD-MM-YYYY (e.g., 12-05 or 12-05-2025 for May 12th 2025)."

    def __init__(self, day: str, month: str, year: str):
        self._day = day
        self._month = month
        self._year = year

    @classmethod
    def _parse(cls, value: str):
        if not re.match(
            r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])(-\d{4})?$", value.strip()
        ):
            return None

        if not re.search(r"-\d{4}", value):
            value += f"-{datetime.now().year}"

        day, month, year = value.strip().split("-")
        return Date(day, month, year)

    def __str__(self):
        return f"{self._day}-{self._month}-{self._year}"

    def __eq__(self, value):
        return str(self) == str(value)
