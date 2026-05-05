from fastapi import APIRouter
from app.schemas.chat import ChatRequest
from app.services.ai_service import get_ai_response

router = APIRouter()  

@router.post("/")
def chat(req: ChatRequest):
    response = get_ai_response(req.message)
    return {"response": response}