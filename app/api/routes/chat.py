from fastapi import APIRouter
from app.schemas.chat import ChatRequest
from app.services.ai_service import get_ai_response
from app.services.recommendation import recommend_products

router = APIRouter()

@router.post("/")
def chat(req: ChatRequest):
    ai_response = get_ai_response(req.message)
    recommendations = recommend_products(req.message)

    return {
        "response": ai_response,
        "recommendations": recommendations if recommendations else ["No exact match, showing popular items"]
    }