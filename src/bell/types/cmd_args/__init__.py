from abc import ABC, abstractmethod

from typer import BadParameter


class CommandArg(ABC):
    _error_msg = "Bad Argument."

    @classmethod
    @abstractmethod
    def _parse(cls, value: str):
        pass

    @classmethod
    def parser(cls, value: str):
        cmd_arg = cls._parse(value)
        if cmd_arg:
            return cmd_arg
        else:
            raise BadParameter(cls._error_msg)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__str__()})"
