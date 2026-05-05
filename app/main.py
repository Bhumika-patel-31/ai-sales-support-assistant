from fastapi import FastAPI
from app.api.routes import chat, recommend
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Business Assistant API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API is running"}

# include routes
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(recommend.router, prefix="/recommend", tags=["Recommend"])