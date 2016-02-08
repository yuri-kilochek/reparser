__all__ = (
    'Then',
)

from ._Parser import *

class Then(Parser):
    __slots__ = (
        '__left',
        '__right',
    )

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        assert isinstance(left, Parser)
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        assert isinstance(right, Parser)
        self.__right = right

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def _parse(self, context):
        for left_text, right_text in context.text.partitions:
            for left_result in context.parse(self.__left, text=left_text):
                for right_result in context.parse(self.__right, text=right_text):
                     yield left_result + right_result

