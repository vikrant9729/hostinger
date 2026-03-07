def detect_industry(prompt):

    prompt = prompt.lower()

    if "restaurant" in prompt or "food" in prompt:
        return "restaurant"

    if "portfolio" in prompt:
        return "portfolio"

    if "agency" in prompt:
        return "agency"

    if "startup" in prompt or "saas" in prompt:
        return "startup"

    if "shop" in prompt or "store" in prompt:
        return "ecommerce"

    return "general"