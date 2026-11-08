def check_discount(subtotal: int) -> float:
    if subtotal > 500:
        discount = subtotal * 0.15
    elif subtotal > 200:
        discount = subtotal * 0.10
    else:
        discount = 0
    return discount


def calculate_total(items):
    Subtotal = sum(i['price'] for i in items)

    discount = check_discount(Subtotal)

    return Subtotal - discount