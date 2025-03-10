from models.product import Product
from constants.constants import CURRENCY


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

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity
        self._calculate_total()

    def set_product(self, new_product):
        self.product = new_product
        self._calculate_total()

    def __repr__(self):
        return f'{self.product.name} {self.item_total_price} {CURRENCY}'
