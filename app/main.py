from fastapi import FastAPI
from app.api.routes import chat, recommend

app = FastAPI(title="AI Business Assistant API")

@app.get("/")
def home():
    return {"message": "API is running"}

# include routes
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(recommend.router, prefix="/recommend", tags=["Recommend"])