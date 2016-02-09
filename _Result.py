__all__ = (
    'Result',
)

class Result:
    __slots__ = (
        '__values',
    )

    @property
    def values(self):
        return self.__values

    @classmethod
    def make_from_value(cls, value):
        return cls((value,))

    def __init__(self, values):
        self.__values = values

    def __eq__(self, other):
        return self.__values == other.__values

    def __hash__(self):
        return hash(self.__values)

    def __add__(self, other):
        if not self.__values:
            return other
        if not other.__values:
            return self
        return Result(self.__values + other.__values)

    def __xor__(self, transform):
        return Result(tuple(transform(*self.__values)))

Result.empty = Result(())

