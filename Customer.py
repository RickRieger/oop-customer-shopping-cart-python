from ShoppingCart import ShoppingCart


class Customer:

    def __init__(self, name):
        self.name = name
        self.shopping_cart = ShoppingCart()

    def add_new_product(self, item):
        print(item)
        self.shopping_cart.add_item_to_cart(item) 

    def view_all_products(self):
        for item in self.shopping_cart.products:
            print(item.name, item.price, item.category)
        