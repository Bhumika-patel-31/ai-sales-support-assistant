import json

def recommend_products(query: str):
    with open("data/products.json") as f:
        products = json.load(f)

    query = query.lower()

    keywords = {
    "sports": ["sports", "gym", "fitness", "exercise", "shoes", "running"],
    "electronics": ["laptop", "computer", "tech"],
    "clothing": ["shirt", "tshirt", "clothes"]
}

    results = []

    for product in products:
        category = product["category"]

        if category in keywords:
            if any(word in query for word in keywords[category]):
                results.append(product)

    return results