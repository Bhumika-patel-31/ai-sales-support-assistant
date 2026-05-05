from fastapi import APIRouter
from app.services.recommendation import recommend_products

router = APIRouter()

@router.get("/")
def recommend(query: str):
    results = recommend_products(query)
    return {"results": results}