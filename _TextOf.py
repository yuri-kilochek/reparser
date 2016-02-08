__all__ = (
    'TextOf',
)

from ._Parser import *
from ._MatchResult import *

class TextOf(Parser):
    __slots__ = (
        '__subject',
    )

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        assert isinstance(subject, Parser)
        self.__subject = subject

    def __init__(self, subject):
        self.subject = subject

    def _parse(self, context):
        for result in context.parse(self.__subject, Result=MatchResult):
            yield context.Result.make_from_value(context.text)

