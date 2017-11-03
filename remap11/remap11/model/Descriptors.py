from remap11.remap11.model.Fields import Name


class Desc:
    def __init__(self, *, path) -> None:
        self.path = path


class ProductDesc(Desc):
    def __init__(self) -> None:
        self.name = Name()
        super().__init__(path='entity/product')


class ProductFolderDesc(Desc):
    def __init__(self) -> None:
        super().__init__(path='entity/productfolder')


product = ProductDesc()
productFolder = ProductFolderDesc()
