__all__ = (
    'Result',
)

from itertools import chain

class Result(tuple):
    __slots__ = ()

    @staticmethod
    def from_lazy_value(lazy_value):
        value = lazy_value()
        return Result([value])

    def __add__(self, right):
        if not self:
            return right
        if not right:
            return self
        return Result(chain(self, right))

    def __xor__(self, function):
        return Result(function(*self))

Result.empty = Result()

