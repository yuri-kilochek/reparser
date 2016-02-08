__all__ = (
    'MatchResult',
)

class MatchResult:
    __slots__ = ()

    @classmethod
    def make_from_value(cls, value):
        return cls.empty

    def __add__(self, other):
        return self

    def __xor__(self, transform):
        return self

MatchResult.empty = MatchResult()
