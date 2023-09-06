from decimal import Decimal

class CashRegister:

    def __init__(self, discount=0):
        self.total = Decimal('0')
        self.discount = Decimal(str(discount))
        self.items = []
        self.transactions = []

    def add_item(self, title, price, quantity=1):
        price = Decimal(str(price))
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.transactions.append({'title': title, 'price': price, 'quantity': quantity})

    def apply_discount(self):
        if self.discount:
            self.total = self.total - (self.total * self.discount / 100)
            print(f"After the discount, the total comes to ${self.total:.2f}")
        else:
            print("There is no discount to apply.")

    def list_items(self):
        return self.items

    def void_last_transaction(self):
        if self.transactions:
            last_transaction = self.transactions.pop()
            self.total -= last_transaction['price'] * last_transaction['quantity']