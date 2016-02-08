__all__ = (
    'Parser',
)

class Parser:
    __slots__ = ()

    def _parse(self, context):
        raise NotImplementedError()
