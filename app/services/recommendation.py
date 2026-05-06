import json

def recommend_products(query: str):
    with open("data/products.json") as f:
        products = json.load(f)

    query = query.lower()

    # ❗ remove useless words
    stopwords = {"for", "the", "and", "i", "want", "need", "something"}
    query_words = [word for word in query.split() if word not in stopwords]

    keywords = {
        "sports": ["sports", "gym", "fitness", "exercise", "shoes", "running"],
        "electronics": ["laptop", "computer", "tech", "headphones", "mobile"],
        "clothing": ["shirt", "tshirt", "clothes", "jeans", "jacket"],
        "accessories": ["watch", "bag", "backpack"],
        "furniture": ["chair", "table", "desk"]
    }

    scored_products = []

    for product in products:
        name = product["name"].lower()
        category = product["category"]

        score = 0

        # ✅ match with product name
        for word in query_words:
            if word in name:
                score += 2

        # ✅ match with category keywords
        if category in keywords:
            for word in query_words:
                if word in keywords[category]:
                    score += 1

        if score > 0:
            scored_products.append((score, product))

    # ✅ sort by relevance
    scored_products.sort(reverse=True, key=lambda x: x[0])

    results = [p for _, p in scored_products]

    # ✅ fallback
    if not results:
        results = products[:4]

    return results[:4]