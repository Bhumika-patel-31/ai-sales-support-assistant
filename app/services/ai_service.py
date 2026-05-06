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
                "content": """ You are an AI sales assistant for an e-commerce store.

                            Guidelines:
                            - Give helpful, natural, medium-length responses (not too short, not too long)
                            - Understand user intent and explain briefly
                            - Suggest suitable product types (not specific brands unless needed)
                            - Be conversational but professional
                            - Do NOT ask too many follow-up questions
                            - Help user make a decision
                            """
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )
    return response.choices[0].message.content