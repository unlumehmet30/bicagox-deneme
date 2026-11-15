def is_reserved(expires_at: int, now: int) -> bool:
    """Report whether a stock reservation still holds its quantity."""
    if expires_at < 0:
        raise ValueError("expiry must be nonnegative")
    return expires_at > now
