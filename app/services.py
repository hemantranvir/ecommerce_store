import uuid
from app.store import carts, orders, discount_codes, NTH_ORDER, DISCOUNT_PERCENT


def add_item(user_id, item):
    if user_id not in carts:
        carts[user_id] = []
    carts[user_id].append(item)


def checkout(user_id, discount_code=None):
    if user_id not in carts or not carts[user_id]:
        raise Exception("Cart is empty")

    cart = carts[user_id]
    total = sum(i["price"] * i["quantity"] for i in cart)
    discount = 0

    if discount_code:
        if discount_code not in discount_codes:
            raise Exception("Invalid code")
        if discount_codes[discount_code]["used"]:
            raise Exception("Code used")

        percent = discount_codes[discount_code]["percent"]
        discount = total * percent / 100
        discount_codes[discount_code]["used"] = True

    order = {
        "id": str(uuid.uuid4()),
        "items": cart,
        "total": total,
        "discount": discount,
        "final": total - discount
    }

    orders.append(order)
    carts[user_id] = []

    return order


def generate_discount():
    if len(orders) % NTH_ORDER != 0:
        return None

    code = str(uuid.uuid4())[:8]
    discount_codes[code] = {"percent": DISCOUNT_PERCENT, "used": False}
    return code


def stats():
    total_items = sum(i["quantity"] for o in orders for i in o["items"])
    revenue = sum(o["final"] for o in orders)
    discounts = sum(o["discount"] for o in orders)

    return {
        "items": total_items,
        "revenue": revenue,
        "discounts": discounts,
        "codes": discount_codes
    }
