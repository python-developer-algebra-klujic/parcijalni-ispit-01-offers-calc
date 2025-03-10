from typing import List
from datetime import datetime as dt

from models.offer_item import OfferItem
from models.customer import Customer
from constants.constants import TAX, CURRENCY


class Offer:
    def __init__(self,
                 customer: Customer,
                 date: dt = dt.now(),
                 offer_items: List[OfferItem] = []):
        self.customer = customer
        self.offer_items = offer_items

        self.id = 1
        self.offer_number = ''
        self.date = date
        self.sub_total = 0.0
        self.tax = 0.0
        self.total = 0.0

        self.calculate_price()
        self.generate_offer_number()

    def generate_offer_number(self):
        # OFFER 2025-03-001
        self.offer_number = f'OFFER {self.date.strftime('%Y-%m')}-{str(self.id).zfill(3)}'

    def add_item(self, item):
        self.offer_items.append(item)
        self.calculate_price()

    def calculate_price(self):
        for item in self.offer_items:
            self.sub_total += item.item_total_price

        self.tax = self.sub_total * (TAX / 100)
        self.total = self.tax + self.sub_total

    def set_offer_date(self, new_date: dt):
        self.date = new_date
        self.generate_offer_number()

    def __repr__(self):
        return f'{self.offer_number} {self.total} {CURRENCY}'
