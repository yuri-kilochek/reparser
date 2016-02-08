__all__ = (
    'TransformedBy',
)

from ._Parser import *

class TransformedBy(Parser):
    __slots__ = (
        '__subject',
        '__function',
    )

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        assert isinstance(subject, Parser)
        self.__subject = subject

    @property
    def function(self):
        return self.__function

    @function.setter
    def function(self, function):
        assert callable(function)
        self.__function = function

    def __init__(self, subject, function):
        self.subject = subject
        self.function = function

    def _parse(self, context):
        for result in context.parse(self.subject):
            yield result ^ self.function

