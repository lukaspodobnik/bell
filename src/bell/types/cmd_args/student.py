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
        parts = list(map(str.capitalize, value.strip().split()))
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
