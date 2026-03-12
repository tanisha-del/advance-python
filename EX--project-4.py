'''.E-Commerce Order Management 
Manage orders, returns, and refunds. 
Handle cases like invalid coupon code, out-of-stock errors, invalid payment 
methods.'''

products = {
    "laptop": 5,
    "phone": 10,
    "headphones": 7
}

coupons = ["SAVE10", "DISCOUNT"]

payments = ["card", "upi", "cod"]

orders = []

def place_order(product, quantity, coupon, payment):

    try:
        if product not in products:
            raise Exception("Product not available")

        if products[product] < quantity:
            raise Exception("Out of stock")

        if coupon != "" and coupon not in coupons:
            raise Exception("Invalid coupon code")

        if payment not in payments:
            raise Exception("Invalid payment method")

        products[product] -= quantity

        order = {
            "product": product,
            "quantity": quantity,
            "status": "Ordered"
        }

        orders.append(order)

        print("Order placed successfully!")

    except Exception as e:
        print("Error:", e)


def return_order(order_id):
    try:
        order = orders[order_id]
        order["status"] = "Returned"
        print("Order returned successfully")

    except:
        print("Invalid order ID")


def refund(order_id):
    try:
        order = orders[order_id]

        if order["status"] != "Returned":
            raise Exception("Refund allowed only after return")

        order["status"] = "Refunded"
        print("Refund completed")

    except Exception as e:
        print("Error:", e)


place_order("laptop", 1, "SAVE10", "card")
place_order("phone", 20, "", "upi")
place_order("headphones", 1, "WRONG", "upi")

return_order(0)
refund(0)
