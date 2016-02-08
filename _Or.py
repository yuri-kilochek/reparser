__all__ = (
    'Or',
)

from ._Parser import *

class Or(Parser):
    __slots__ = (
        '__some',
        '__other',
    )

    @property
    def some(self):
        return self.__some

    @some.setter
    def some(self, some):
        assert isinstance(some, Parser)
        self.__some = some

    @property
    def other(self):
        return self.__other

    @other.setter
    def other(self, other):
        assert isinstance(other, Parser)
        self.__other = other

    def __init__(self, some, other):
        self.some = some
        self.other = other

    def _parse(self, context):
        yield from context.parse(this.some)
        yield from context.parse(this.other)

