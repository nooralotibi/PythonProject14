import pytest
from Discount import calculate_total  # تأكدي أن اسم الملف يطابق اسم ملفك الأساسي


@pytest.mark.parametrize("subtotal_price, expected_final", [
    (600, 510.0),  # حالة 1: أكبر من 500 (خصم 15%)
    (300, 270.0),  # حالة 2: بين 200 و 500 (خصم 10%)
    (150, 150.0),  # حالة 3: أقل من 200 (بدون خصم)
])
def test_calculate_total_parameterized(subtotal_price, expected_final):
    items = [{'price': subtotal_price, 'quantity': 1}]

    # pytest يشغل هذا الاختبار 3 مرات تلقائياً لكل صف في الجدول
    assert calculate_total(items) == expected_final