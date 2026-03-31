from pydantic import BaseModel
from typing import Optional


class AddToCartRequest(BaseModel):
    user_id: str
    item_id: str
    price: float
    quantity: int


class CheckoutRequest(BaseModel):
    user_id: str
    discount_code: Optional[str] = None
