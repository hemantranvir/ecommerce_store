from fastapi import APIRouter
from app.services import generate_discount, stats

router = APIRouter(prefix="/admin")


@router.post("/generate-discount")
def gen():
    code = generate_discount()
    if not code:
        return {"message": "Condition not met"}
    return {"code": code}


@router.get("/stats")
def get():
    return stats()
