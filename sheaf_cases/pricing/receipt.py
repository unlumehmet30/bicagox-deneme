from sheaf_cases.pricing.quote import build_quote


def print_receipt(subtotal: int, requested: int, delivery_fee: int) -> str:
    """Format the customer receipt using the checkout calculation."""
    quote = build_quote(subtotal, requested, delivery_fee)
    total = quote["total"]
    discount = quote["discount"]
    return f"total={total}; discount={discount}"
