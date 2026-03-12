'''Custom Exception Framework 
Create your own custom exceptions for a specific application (like an Inventory 
Management System). 
For example: OutOfStockError, InvalidProductIDError, etc.'''


class OutOfStockError(Exception):
    pass

class InvalidProductIDError(Exception):
    pass

inventory = {
    101: {"name": "Laptop", "stock": 5},
    102: {"name": "Phone", "stock": 3},
    103: {"name": "Tablet", "stock": 0}
}

def purchase(product_id, quantity):
    try:
        if product_id not in inventory:
            raise InvalidProductIDError("Invalid Product ID")

        if inventory[product_id]["stock"] < quantity:
            raise OutOfStockError("Product out of stock")

        inventory[product_id]["stock"] -= quantity

        print("Purchase successful")
        print("Remaining stock:", inventory[product_id]["stock"])

    except InvalidProductIDError as e:
        print("Error:", e)

    except OutOfStockError as e:
        print("Error:", e)


purchase(101, 2)
purchase(103, 1)
purchase(999, 1)
