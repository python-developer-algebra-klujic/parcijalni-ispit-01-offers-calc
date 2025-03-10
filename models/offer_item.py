from product import Product


class OfferItem:
    def __init__(self,
                 id: int,
                 quantity: int,
                 product: Product):
        self.id = id
        self.quantity = quantity
        self.product = product
        self.item_total_price = 0.0
        self._calculate_total()

    def _calculate_total(self):
        self.item_total_price = self.quantity * self.product.price

    def __repr__(self):
        return f''
