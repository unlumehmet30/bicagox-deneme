from sheaf_cases.inventory.holding import is_reserved


def available_stock(stock: int, reservations: list[tuple[int, int]], now: int) -> int:
    """Subtract the active quantity from physical stock."""
    held = 0
    for quantity, expiry in reservations:
        if is_reserved(expiry, now):
            held += quantity
    return max(0, stock - held)
