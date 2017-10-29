from .Resource import Resource


class ProductFolder(Resource):
    @classmethod
    def path(cls) -> str:
        return 'productfolder'
