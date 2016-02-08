__all__ = (
    'Text',
)

class Text:
    class Position:
        __slots__ = (
            '__line',
            '__column',
        )

        def __init__(self, line, column):
            self.__line = line
            self.__column = column

    __slots__ = (
        '__string',
        '__start_offset',
        '__stop_offset',
    )

    @peoperty
    def start_offset(self):
        return self.__start_offset

    @peoperty
    def stop_offset(self):
        return self.__stop_offset

    def __init__(self, string, start=None, stop=None):
        assert isinstance(string, str)

        if start is None:
            start = 0
        else:
            assert isinstance(start, int)
            assert start >= 0
            assert start <= len(string)

        if stop is None:
            stop = len(text)
        else:
            assert isinstance(stop, int)
            assert stop >= start
            assert stop <= len(string)

        self.__string = string
        self.__start = start
        self.__stop = stop

    @property
    def before(self):
        return self.__class__(self.__string, stop=self.__start)

    @property
    def after(self):
        return self.__class__(self.__string, start=self.__stop)

    def partition(self):
        for split in range(self.__start, self.__stop + 1):
            left = self.__class__(self.__string, self.__start, split)
            right = self.__class__(self.__string, split, self.__stop)
            yield left, right

    def __bool__(self):
        return self.__start < self.__stop

    def __str__(self):
        return self.__string[self.__start:self.__stop]

    def __len__(self):
        return self.__stop - self.__start


    def __getitem__(self, index):
        raise NotImplementedError()

