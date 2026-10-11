from business_rules import (
    apply_discount,
    calculate_total,
    get_approval_tier,
    requires_review,
)


def test_total_includes_tax():
    assert round(calculate_total(100.00, 2), 2) == 214.00  # 200 * 1.07


def test_requires_review_over():
    assert requires_review(1500) is True


def test_requires_review_under():
    assert requires_review(500) is False


def test_boundary_at_limit():  # BOUNDARY: exactly 1000 is NOT over (> not >=)
    assert requires_review(1000) is False


def test_boundary_one_above():  # BOUNDARY: one cent above flips it
    assert requires_review(1000.01) is True


def test_tier_auto():
    assert get_approval_tier(400) == "auto"


def test_tier_boundary_500():  # BOUNDARY: exactly at the 500 edge
    assert get_approval_tier(500) == "auto"


def test_discount_ten():
    assert apply_discount(100.00, 10) == 90.0
