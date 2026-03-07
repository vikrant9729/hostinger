from app.services.ai_generator import generate_ai_website


def generate_layout(prompt):

    layout_prompt = f"""
Create a website layout structure for:

{prompt}

Sections order:

Navbar
Hero
Features
Pricing
Testimonials
Gallery
Contact
Footer

Return only HTML sections.
"""

    return generate_ai_website(layout_prompt)