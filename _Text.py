__all__ = (
    'Text',
)


class Text(str):
    __slots__ = (
        '__positions',
    )

    @property
    def positions(self):
        return self.__positions

    def __init__(self, *args, **kwargs):
        positions = []

        line = 0
        column = 0
        for character in self:
            positions.append((line, column))
            if character == '\n':
                line += 1
                column = 0
            else:
                column += 1
        positions.append((line, column))

        self.__positions = tuple(positions)


class TextSlice(str):
    __slots__ = (
        '__text',
        '__start',
        '__stop',
        '__partitions',
    )

    @property
    def text(self):
        return self.__text

    @property
    def start(self):
        return self.__start

    @property
    def start_position(self):
        return self.__text.positions[self.__start]

    @property
    def stop(self):
        return self.__stop

    @property
    def stop_position(self):
        return self.__text.positions[self.__stop]

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, text, start=None, stop=None):
        assert isinstance(text, Text)

        if start is None:
            start = 0
        else:
            assert isinstance(start, int)
            assert start >= 0
            assert start <= len(text)

        if stop is None:
            stop = len(text)
        else:
            assert isinstance(stop, int)
            assert stop >= start
            assert stop <= len(text)

        self.__text = text
        self.__start = start
        self.__stop = stop
        self.__partitions = None

    @property
    def before(self):
        return TextSlice(self.__text, stop=self.__start)

    @property
    def after(self):
        return TextSlice(self.__text, start=self.__stop)

    @property
    def partitions(self):
        if self.__partitions is None:
            partitions = []
            for cut in range(self.__start, self.__stop + 1):
                left = TextSlice(self.__text, self.__start, cut)
                right = TextSlice(self.__text, cut, self.__stop)
                partitions.append((left, right))
            self.__partitions = tuple(partitions)
        return self.__partitions

    def __str__(self):
        return str(self.__text[self.__start:self.__stop])

    def __repr__(self):
        return repr(str(self))


s = 'foo\nbar'
for x in TextSlice(Text(s)).partitions:
    print(x)

