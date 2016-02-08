__all__ = (
    'EmptyString',
)

from ._Parser import *

class EmptyString(Parser):
    __slots__ = ()

    def _parse(self, context):
        if not context.text:
            yield context.Result.empty

