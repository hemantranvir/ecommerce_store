from app.services import add_item, checkout, generate_discount
from app.store import carts, orders, discount_codes


def setup_function():
    carts.clear()
    orders.clear()
    discount_codes.clear()


def test_checkout_without_discount():
    user = "u1"
    add_item(user, {"item_id": "i1", "price": 100, "quantity": 1})
    result = checkout(user)
    assert result["final"] == 100
    assert result["discount"] == 0


def test_generate_discount_on_nth_order():
    user = "u1"

    # Create NTH_ORDER orders
    for _ in range(3):
        add_item(user, {"item_id": "i1", "price": 100, "quantity": 1})
        checkout(user)

    code = generate_discount()
    assert code is not None
    assert code in discount_codes


def test_apply_valid_discount_code():
    user = "u1"

    # Generate discount
    for _ in range(3):
        add_item(user, {"item_id": "i1", "price": 100, "quantity": 1})
        checkout(user)

    code = generate_discount()

    # Apply discount
    add_item(user, {"item_id": "i2", "price": 200, "quantity": 1})
    result = checkout(user, code)

    assert result["discount"] > 0
    assert result["final"] == 200 - result["discount"]


def test_invalid_discount_code():
    user = "u1"
    add_item(user, {"item_id": "i1", "price": 100, "quantity": 1})

    try:
        checkout(user, "invalid")
    except Exception as e:
        assert "Invalid" in str(e)


def test_reuse_discount_code_fails():
    user = "u1"

    # Generate discount
    for _ in range(3):
        add_item(user, {"item_id": "i1", "price": 100, "quantity": 1})
        checkout(user)

    code = generate_discount()

    # First use
    add_item(user, {"item_id": "i2", "price": 100, "quantity": 1})
    checkout(user, code)

    # Reuse should fail
    add_item(user, {"item_id": "i3", "price": 100, "quantity": 1})
    try:
        checkout(user, code)
    except Exception as e:
        assert "used" in str(e)
