from abc import ABCMeta, abstractmethod


class Resource(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def path(cls) -> str:
        pass
