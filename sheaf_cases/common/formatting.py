def format_percent(value: float) -> str:
    return f"{value * 100:.0f}%"


def format_total(subtotal: int, fee: int, adjustment: int) -> str:
    return str(subtotal + fee - adjustment)
