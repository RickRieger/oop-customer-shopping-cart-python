
class ShoppingCart:
    def __init__(self):
        self.products = []

    def return_total(self):
        total = 0
        for item in self.products:
            total += item.price
        return total    

    def add_item_to_cart(self, item):
        self.products.append(item) 

    def empty_shopping_cart(self):
        self.products = []           