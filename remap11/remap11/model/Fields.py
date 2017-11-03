from .Field import Field


class StringField(Field):
    def __init__(self, name: str):
        super().__init__(name, str)


class FloatField(Field):
    def __init__(self, name: str):
        super().__init__(name, float)


class IntField(Field):
    def __init__(self, name: str):
        super().__init__(name, int)


class Name(StringField):

    def __init__(self):
        super().__init__('name')

    def _check(self, val):
        if val is None or not isinstance(val, str) or len(val.trim()) == 0:
            raise AttributeError('Field name can''t be None or empty')
        return val
