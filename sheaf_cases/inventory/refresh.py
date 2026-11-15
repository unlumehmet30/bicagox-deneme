def next_inventory_refresh(expiry: int, now: int, interval: int) -> int:
    """Choose a polling time for the stock availability view."""
    if expiry <= now:
        return now + interval
    return min(now + interval, expiry)


def format_inventory_time(now: int) -> str:
    return f"Inventory updated at {now}"
