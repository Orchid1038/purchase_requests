class calculate_cost:
    def __init__(self, unit_price, quantity):
        self.unit_price = unit_price
        self.quantity = quantity

    def total_cost(self):
        return self.unit_price * self.quantity