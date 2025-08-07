from abc import ABC, abstractmethod

from typer import BadParameter


class CommandArg(ABC):
    def __init__(self, value: str, error_msg: str):
        if not self.is_valid(value):
            raise BadParameter(error_msg)

    @abstractmethod
    def is_valid(self, value: str) -> bool:
        pass

    def __str__(self):
        return " ".join(map(lambda x: str(x), vars(self).values()))

    @classmethod
    def parse(cls, value: str):
        return cls(value)
