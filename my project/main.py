
from config import APP_NAME, VERSION, CURRENCY

from services.calculator import (
    calculate_total,
    calculate_discount
)

from utils.formatter import format_money


def main():
    print("=" * 40)
    print(APP_NAME)
    print(f"Версія: {VERSION}")
    print("=" * 40)

    price = 500
    quantity = 4
    discount = 15

    total = calculate_total(price, quantity)
    final_price = calculate_discount(total, discount)

    print(f"Ціна товару: {format_money(price, CURRENCY)}")
    print(f"Кількість: {quantity}")
    print(f"До знижки: {format_money(total, CURRENCY)}")
    print(f"Знижка: {discount}%")
    print(f"До оплати: {format_money(final_price, CURRENCY)}")


if __name__ == "__main__":
    main()
