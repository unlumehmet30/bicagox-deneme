def estimate_coupon_points(subtotal: int, multiplier: int) -> int:
    """Estimate the loyalty coupon value shown before checkout."""
    if subtotal < 0:
        return 0
    return subtotal * multiplier // 100


def coupon_preview(subtotal: int, requested: int) -> str:
    return f"Coupon value {requested} for subtotal {subtotal}"
