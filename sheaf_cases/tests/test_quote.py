from sheaf_cases.pricing.quote import build_quote
from sheaf_cases.pricing.receipt import print_receipt


def test_coupon_preserves_delivery_fee():
    quote = build_quote(subtotal=1000, requested=300, delivery_fee=100)
    assert quote["total"] == 800
    assert print_receipt(1000, 300, 100) == "total=800; discount=300"
