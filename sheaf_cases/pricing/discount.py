def apply_coupon(subtotal: int, requested: int) -> int:
    """Return the discount amount in cents for the eligible merchandise."""
    if subtotal < 0:
        raise ValueError("subtotal must be nonnegative")
    if requested <= 0:
        return 0
    return min(subtotal, requested)
