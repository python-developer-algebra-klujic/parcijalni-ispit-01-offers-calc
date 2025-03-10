


class Customer:
    def __init__(self,
                 id: int,
                 name: str,
                 email: str,
                 vat_id: str):
        self.id = id
        self.name = name
        self.email = email
        self.vat_id = vat_id

    def __repr__(self):
        return f'Korisnik {self.name} ({self.email})'
