from fastapi import APIRouter

router = APIRouter(
    prefix="/review",
    tags=["Review"]
)

@router.get("/")  # Ejemplo: localhost:8000/review/
async def get_reviews_root():
    return {"mensaje": "Endpoint raíz de reviews"}