
def format_money(amount: float, currency: str = "грн") -> str:
    return f"{amount:,.2f} {currency}"
