import re

from bell.types.cmd_args import CommandArg


class Student(CommandArg):
    _error_msg = (
        "Expected format: first_name last_name "
        "(e.g. Max Mustermann). Multiple first names are allowed."
    )

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def _parse(cls, value: str):
        parts = value.strip().split()
        if len(parts) < 2:
            return None

        return Student(" ".join(parts[:-1]), parts[-1])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):
        return (
            isinstance(other, Student)
            and self.first_name == other.first_name
            and self.last_name == other.last_name
        )

    def __hash__(self):
        return hash((self.first_name, self.last_name))


class Grade(CommandArg):
    _error_msg = "Expected format: a single digit from 1–6 (e.g. 4)."

    def __init__(self, grade: int):
        self.grade = grade

    @classmethod
    def _parse(cls, value: str):
        if not re.match(r"^[1-6]$", value.strip()):
            return None

        return Grade(int(value))

    def __str__(self):
        return str(self.grade)


class Date(CommandArg):
    _error_msg = "Expected format: DD-MM (e.g. 12-05 for May 12th)"

    def __init__(self, day: str, month: str):
        self.day = day
        self.month = month

    @classmethod
    def _parse(cls, value: str):
        print(
            f"This is the value which got passed to _parse: {value}. Its type is {type(value)}"
        )
        if not re.match(r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])$", value.strip()):
            return None

        day, month = value.strip().split("-")
        return Date(day, month)

    def __str__(self):
        return f"{self.day}-{self.month}"


class Slot(CommandArg):
    _error_msg = "Expected: single digit between 1 and 6."

    def __init__(self, num: int):
        self.num = num

    @classmethod
    def _parse(cls, value: str):
        if not re.match(r"^[1-6]$", value.strip()):
            return None

        return Slot(int(value))

    def __str__(self):
        return str(self.num)
