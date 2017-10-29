from .Resource import Resource


class Product(Resource):
    @classmethod
    def path(cls) -> str:
        return 'product'
