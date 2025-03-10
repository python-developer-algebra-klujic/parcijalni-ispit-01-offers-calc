


class Product:
    def __init__(self,
                 id: int,
                 name: str,
                 description: str = '',
                 price: float = 0.00):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self) -> str:
        return f'Proizvod: {self.name} ({self.price} EUR)'
