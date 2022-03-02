from Customer import Customer
from Product import Product


#1. Print the customer’s name to the terminal

customer = Customer('Rick')

print(customer.name)

# 2. Call the customer’s add product to shopping cart method three times and add the three products objects you created

customer.add_new_product(Product('shoes', 100, 'clothes')) 
customer.add_new_product(Product('i-watch', 450, 'electronics')) 
customer.add_new_product(Product('ring', 4500, 'jewelry')) 

# 3. Call the customer’s view products method

customer.view_all_products()

# 4. Call the customer’s shopping cart’s get cart total method. Capture the total the method returns in a variable and print to the terminal

total = customer.shopping_cart.return_total()
print(total)

# 5. Call the customer’s shopping cart’s empty cart method

customer.shopping_cart.empty_shopping_cart()

# 6. Check if all products have been removed from the shopping cart

print('=========IS EMPTY?========')
customer.view_all_products()
