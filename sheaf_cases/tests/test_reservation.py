from sheaf_cases.inventory.available import available_stock
from sheaf_cases.inventory.cart import cart_availability


def test_reservation_boundary():
    held = [(3, 100), (2, 101)]
    assert available_stock(10, held, now=99) == 5
    assert cart_availability(10, held, now=101, requested=6)["can_add"]
