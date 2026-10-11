# business_rules.py
# Author: Theodore Major

APPROVAL_LIMIT = 1000.00  # module-level constant, ALL_CAPS


def calculate_total(price: float, quantity: int) -> float:
    """Return total cost including 7% tax."""
    return price * quantity * 1.07


def requires_review(amount: float) -> bool:
    """Return True if amount exceeds the approval limit."""
    return amount > APPROVAL_LIMIT


def get_approval_tier(amount: float) -> str:
    """Return the approval routing tier for a given amount."""
    if amount <= 500:
        return "auto"
    elif amount <= 2000:
        return "manager"
    else:
        return "director"


def apply_discount(price: float, pct: float) -> float:
    """Return price after a percentage discount. pct is 0-100."""
    return price * (1 - pct / 100)
