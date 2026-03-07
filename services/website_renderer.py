from app.core.database import supabase
from app.services.industry_detector import detect_industry
from app.services.color_engine import generate_colors
from app.services.font_engine import get_font
from app.services.design_ranker import pick_best_section
from app.services.layout_engine import get_layout
from app.services.design_consistency_engine import apply_design_consistency
from app.services.ai_section_modifier import modify_section
from app.services.design_system_engine import generate_design_system

import random


def get_section(category):

    res = supabase.table("sections")\
        .select("*")\
        .eq("category", category)\
        .execute()

    if not res.data:
        return ""

    section = pick_best_section(res.data)

    return section["html_code"]


def get_global_css(design):

    return f"""

<style>

body{{
background:{design["background"]};
color:{design["primary"]};
font-family:{design["font"]};
margin:0;
padding:0;
}}

button{{
background:{design["primary"]};
color:white;
border:none;
padding:12px 24px;
border-radius:{design["button_radius"]};
}}

section{{
padding:80px 20px;
}}

</style>

"""


def render_website(prompt):

    # detect industry
    industry = detect_industry(prompt)

    # design system
    design = generate_design_system(industry)

    # colors
    palette = generate_colors(industry)

    # fonts
    font = get_font(industry)

    # layout
    layout = get_layout(industry)

    sections_html = ""

    for section in layout:

        section_html = get_section(section)

        # AI improve section
        section_html = modify_section(section_html)

        sections_html += section_html

    html = f"""
<!DOCTYPE html>
<html>

<head>

<meta charset="UTF-8">

<title>{prompt}</title>

{get_global_css(design)}

</head>

<body>

{sections_html}

</body>

</html>
"""

    html = apply_design_consistency(html, palette, font)

    return html