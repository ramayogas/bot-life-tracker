from fastapi import APIRouter

router = APIRouter(prefix="/daily", tags=["daily"])

@router.get("/")
def daily_check():
    return {"status": "ok", "service": "life-tracker"}