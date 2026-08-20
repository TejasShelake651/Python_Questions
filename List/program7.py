"""
7. Write a program to develop an inventory system for a small store. Each product has a name and a quantity in stock. The system should allow you to:
● Add new products with their quantities.
● Update the quantity of an existing product.
● Display the product with the highest stock.
● Remove a product from the inventory once it is sold out (quantity reaches 0).
● Display the total number of unique products in the inventory.
Tasks:
● Use a dictionary where the product names are the keys, and the quantities are the values.
● Implement functions for adding, updating, removing, and analyzing inventory.
"""

inventory = {}

def add_product(name, qty):
    inventory[name] = inventory.get(name, 0) + qty

def update_product(name, qty):
    if name in inventory:
        inventory[name] = qty
        if inventory[name] <= 0:
            del inventory[name]

def show_highest():
    if not inventory:
        return None
    return max(inventory, key=inventory.get)

add_product("Apple", 10)
add_product("Banana", 5)
update_product("Banana", 0)
print("Highest stock:", show_highest())
print("Total unique products:", len(inventory))
