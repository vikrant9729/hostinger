import random
from app.core.database import supabase


def get_sections(category):

    res = supabase.table("sections")\
        .select("*")\
        .eq("category", category)\
        .execute()

    sections = res.data

    if not sections:
        return []

    return [random.choice(sections)]