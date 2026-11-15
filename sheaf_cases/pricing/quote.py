from sheaf_cases.pricing.discount import apply_coupon


def build_quote(subtotal: int, requested: int, delivery_fee: int) -> dict:
    """Summarize merchandise and delivery charges for checkout."""
    discount = apply_coupon(subtotal, requested)
    return {
        "merchandise": subtotal,
        "discount": discount,
        "delivery_fee": delivery_fee,
        "total": subtotal - discount + delivery_fee,
    }
