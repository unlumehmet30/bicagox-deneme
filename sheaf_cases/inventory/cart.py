from sheaf_cases.inventory.available import available_stock


def cart_availability(stock, reservations, now, requested):
    """Return a cart view for a quantity request."""
    remaining = available_stock(stock, reservations, now)
    return {"available": remaining, "can_add": requested <= remaining}
