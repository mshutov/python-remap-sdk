from remap11.remap11.Client import Client
from remap11.remap11.model.Descriptors import Desc


class QueryFactory:
    def __init__(self, client: Client) -> None:
        self._client = client

    def query(self, resource: Desc):
        return Query(resource, self._client)

    def new(self, resource: Desc):
        return New(resource, self._client)


class Query:
    def __init__(self, x: Desc, client: Client) -> None:
        self._resource = x
        self._fields = []
        self._client = client

    def select(self, *fields):
        self._fields = fields
        return self

    def list(self):
        return self._client.list(self._resource)['rows']


class New:
    def __init__(self, x: Desc, client: Client) -> None:
        self._resource = x
        self._data = dict()
        self._client = client

    def set(self, *fields_and_values):
        for (field, value) in fields_and_values:
            self._data[field.name] = value
        return self

    def execute(self):
        return self._client.create_or_update(self._resource, self._data)
