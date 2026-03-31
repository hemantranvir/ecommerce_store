from fastapi import APIRouter
from app.models import AddToCartRequest
from app.services import add_item

router = APIRouter(prefix="/cart")


@router.post("/add")
def add(req: AddToCartRequest):
    add_item(req.user_id, req.dict(exclude={"user_id"}))
    return {"message": "added"}
