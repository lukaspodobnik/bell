import re

from bell.types.cmd_args import CommandArg


class Year(CommandArg):
    _error_msg = "Expected format: YYYY-YY (e.g., 2025-26)"

    def __init__(self, school_year: str):
        self.school_year = school_year

    @classmethod
    def _parse(cls, value):
        if not re.match(r"^\d{4}-\d{2}$", value):
            return None

        return Year(value)

    def __str__(self):
        return self.school_year


class Class_(CommandArg):
    _error_msg = "Expected format: ddc - d=digit, c=character (e. g., 10A)"

    def __init__(self, name: str):
        self.name = name

    @classmethod
    def _parse(cls, value):
        if not re.match(r"^\d{1,2}[A-Za-z]$", value):
            return None

        return Class_(value.upper())

    def __str__(self):
        return self.name
