__all__ = (
    'TransformedBy',
)

from ._Parser import *

class TransformedBy(Parser):
    __slots__ = (
        '__subject',
        '__transform',
    )

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        assert isinstance(subject, Parser)
        self.__subject = subject

    @property
    def transform(self):
        return self.__transform

    @transform.setter
    def transform(self, transform):
        assert callable(transform)
        self.__transform = transform

    def __init__(self, subject, transform):
        self.subject = subject
        self.transform = transform

    def _parse(self, context):
        for result in context.parse(self.__subject):
            yield result ^ self.__transform

