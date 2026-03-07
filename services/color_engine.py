import random
from app.core.database import supabase


def generate_colors(industry=None):

    res = supabase.table("color_palettes").select("*").execute()

    if not res.data:

        return {
            "primary_color": "#4F46E5",
            "secondary_color": "#06B6D4",
            "background_color": "#F9FAFB"
        }

    palette = random.choice(res.data)

    return {
        "primary_color": palette.get("primary_color", "#4F46E5"),
        "secondary_color": palette.get("secondary_color", "#06B6D4"),
        "background_color": palette.get("background_color", "#F9FAFB")
    }