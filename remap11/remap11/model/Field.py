from typing import Optional


class Field:
    def __init__(self, name: str, type_):
        self.name = name
        self._type = type_

    def read(self, data: dict) -> Optional:
        return self._convert(data.get([self.name], None))

    def write(self, val, data: dict):
        data[self.name] = self._check(val)

    def _convert(self, val):
        return val

    def _check(self, val):
        if not isinstance(val, self._type):
            raise TypeError()
        return val
