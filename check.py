class Checkout:
    def __init__(self, id, isbn):
        self.id = id
        self.isbn = isbn

    def __str__(self):
        return f"user_id: {self.user_id}, isbn: {self.isbn}"

class CheckoutManager:
    def __init__(self):
        checkouts = []
        checkins = []

    def checkin_book(self, user_id, isbn):
        new_checkout = Checkout(user_id, isbn)
        self.checkins.append(new_checkout)

    def checkout_book(self, user_id, isbn):
        new_checkout = Checkout(user_id, isbn)
        self.checkouts.append(new_checkout)
