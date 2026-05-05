import json

def recommend_products(query: str):
    with open("data/products.json") as f:
        products = json.load(f)

    return [p for p in products if query.lower() in p["category"]]