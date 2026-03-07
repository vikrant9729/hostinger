def classify_section(html):

    html = html.lower()

    if "<nav" in html:
        return "navbar"

    if "hero" in html or "banner" in html:
        return "hero"

    if "feature" in html or "service" in html:
        return "features"

    if "pricing" in html or "price" in html:
        return "pricing"

    if "gallery" in html or "portfolio" in html:
        return "gallery"

    if "testimonial" in html:
        return "testimonials"

    if "faq" in html:
        return "faq"

    if "contact" in html or "form" in html:
        return "contact"

    if "<footer" in html:
        return "footer"

    return "generic"