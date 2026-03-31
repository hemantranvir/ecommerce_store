from fastapi import APIRouter, HTTPException
from app.models import CheckoutRequest
from app.services import checkout

router = APIRouter()


@router.post("/checkout")
def do_checkout(req: CheckoutRequest):
    try:
        return checkout(req.user_id, req.discount_code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
