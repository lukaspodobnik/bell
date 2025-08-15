import re

from bell.types.cmd_args import CommandArg


class Class_(CommandArg):
    _error_msg = "Expected format: a number followed by a letter (e.g., 10A or 9B)."

    def __init__(self, name: str):
        self._name = name

    @classmethod
    def _parse(cls, value):
        if not re.match(r"^\d{1,2}[A-Za-z]$", value):
            return None

        return Class_(value.upper())

    def __str__(self):
        return self._name
