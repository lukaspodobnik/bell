import re

from bell.types.cmd_args import CommandArg


class Year(CommandArg):
    def __init__(self, value: str):
        super().__init__(value, error_msg="Expected format: YYYY-YY (e.g., 2025-26)")
        self.value = value

    def is_valid(self, value):
        return re.match(r"^\d{4}-\d{2}$", value) is not None


class Class_(CommandArg):
    def __init__(self, value: str):
        super().__init__(
            value, error_msg="Expected format: ddc - d=digit, c=character (e. g., 10A)"
        )
        self.value = value

    def is_valid(self, value):
        return re.match(r"^\d{1,2}[A-Za-z]$", value) is not None
