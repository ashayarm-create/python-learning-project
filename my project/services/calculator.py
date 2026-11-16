
def calculate_total(price: float, quantity: int) -> float:
    if price < 0 or quantity < 0:
        raise ValueError("Ціна та кількість не можуть бути від'ємними")

    return price * quantity


def calculate_discount(total: float, discount: float) -> float:
    if not 0 <= discount <= 100:
        raise ValueError("Знижка має бути від 0 до 100%")

    return total - (total * discount / 100)
