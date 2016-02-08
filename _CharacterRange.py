__all__ = (
    'CharacterRange',
)

from ._Parser import *

class CharacterRange(Parser):
    __slots__ = (
        '__start',
        '__stop',
    )

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        assert isinstance(start, str)
        assert len(start) == 1
        self.__start = start
        if self.__stop < start:
            self.__stop = start

    @property
    def stop(self):
        return self.__stop

    @stop.setter
    def stop(self, stop):
        assert isinstance(stop, str)
        assert len(stop) == 1
        self.__stop = stop
        if self.__start > stop:
            self.__start = stop

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def _parse(self, context):
        if len(context.text) == 1 and self.start <= str(context.text) <= self.stop:
            yield context.Result.empty

