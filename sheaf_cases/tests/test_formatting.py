from sheaf_cases.common.formatting import format_percent, format_total


def test_checkout_total_label():
    assert format_total(100, 10, 30) == "80"


def test_delivery_percentage_label():
    assert format_percent(0.5) == "50%"
