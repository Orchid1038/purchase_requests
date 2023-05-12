#
class PurchaseRequest:
    def __init__(self, department, item, unit_price, quantity, purpose, name, note):
        self.department = department
        self.item = item
        self.quantity = quantity
        self.purpose = purpose
        self.purchaser = name
        self.name = name
        self.unit_price = unit_price
        self.note = note
        self.purchased = False
        self.approved = False

    def approve(self):
        self.approved = True
        print("Purchase request for " + self.item + " has been approved.")

    def reject(self):
        print("Purchase request for " + self.item + " has been rejected.")


    def __str__(self):
        return "Department: " + self.department + "\n" \
               "Item: " + self.item + "\n" \
               "Unit_price" + self.unit_price + "\n" \
               "Quantity: " + str(self.quantity) + "\n" \
               "Purpose: " + self.purpose + "\n" \
               "Purchaser: " + self.purchaser + "\n" \
               "Approved: " + str(self.approved)
