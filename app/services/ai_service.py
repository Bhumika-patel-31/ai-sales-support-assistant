from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def get_ai_response(message: str) -> str:
    response = client.chat.completions.create(
        model="meta-llama/llama-3-8b-instruct",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant that helps customers choose products and increases sales by recommending relevant items."
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )
    return response.choices[0].message.content