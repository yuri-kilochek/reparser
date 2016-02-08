__all__ = (
    'EmptyString',
)

from ._Parser import *

class EmptyString(Parser):
    __slots__ = ()

    def _parse(self, context):
        if len(context.text) == 0:
            yield context.Result.empty

