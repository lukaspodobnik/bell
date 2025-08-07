import re

from bell.types.cmd_args import CommandArg


class Student(CommandArg):
    def __init__(self, value: str):
        super().__init__(
            value,
            error_msg="Expected format: first_name last_name - e. g. Max Musterman. Also accepts multiple first_names - e. g. Max Moritz Musterman.",
        )
        full_name = value.split()
        self.first_name = " ".join(full_name[:-1])
        self.last_name = full_name[-1]

    def is_valid(self, value: str) -> bool:
        return len(value.split()) >= 2


class Grade(CommandArg):
    def __init__(self, value: str):
        super().__init__(
            value, error_msg="Expected format: d - a singular digit from 1-6."
        )
        self.value = value

    def is_valid(self, value):
        return re.match(r"^[1-6]$", value) is not None


class Date(CommandArg):
    def __init__(self, value: str):
        super().__init__(
            value,
            error_msg="Expected format: DD-MM - e. g. 12.05 for the twelfth of may.",
        )
        self.value = value

    def is_valid(self, value):
        return (
            re.match(r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])$", value) is not None
        )


class Slot(CommandArg):
    def __init__(self, value: str):
        super().__init__(value, error_msg="Expected: single digit between 1 and 6.")
        self.value = value

    def is_valid(self, value):
        return re.match(r"^[1-6]$", value) is not None
