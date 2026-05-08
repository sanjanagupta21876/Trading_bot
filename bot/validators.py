def validate_side(side):
    valid_sides = ["BUY", "SELL"]

    if side.upper() not in valid_sides:
        raise ValueError("Side must be BUY or SELL")


def validate_order_type(order_type):
    valid_types = ["MARKET", "LIMIT"]

    if order_type.upper() not in valid_types:
        raise ValueError("Order type must be MARKET or LIMIT")


def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")


def validate_price(order_type, price):
    if order_type.upper() == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")

        if price <= 0:
            raise ValueError("Price must be greater than 0")