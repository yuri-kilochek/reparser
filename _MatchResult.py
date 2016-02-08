__all__ = (
    'MatchResult',
)

from ._Result import *

class MatchResult(Result):
    __slots__ = ()

    @staticmethod
    def from_lazy_value(lazy_value):
        return MatchResult.empty

    def __add__(self, right):
        return MatchResult.empty

    def __xor__(self, function):
        return MatchResult.empty

MatchResult.empty = MatchResult()
