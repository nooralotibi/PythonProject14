import pytest
from Discount import calculate_total  #


@pytest.mark.parametrize("subtotal_price, expected_final", [
    (600, 510.0),  #
    (300, 270.0),  #
    (150, 150.0),  #
])
def test_calculate_total_parameterized(subtotal_price, expected_final):
    items = [{'price': subtotal_price, 'quantity': 1}]

    assert calculate_total(items) == expected_final