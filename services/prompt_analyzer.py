def analyze_prompt(prompt):

    prompt = prompt.lower()

    industry = "general"
    style = "modern"
    features = []

    if "restaurant" in prompt:
        industry = "restaurant"

    if "saas" in prompt:
        industry = "saas"

    if "portfolio" in prompt:
        industry = "portfolio"

    if "ecommerce" in prompt or "shop" in prompt:
        industry = "ecommerce"

    if "booking" in prompt:
        features.append("booking")

    if "gallery" in prompt:
        features.append("gallery")

    if "contact" in prompt:
        features.append("contact")

    return {
        "industry": industry,
        "style": style,
        "features": features
    }