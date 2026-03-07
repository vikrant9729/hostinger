from app.core.database import supabase
from app.services.section_classifier import detect_category


def clean_database():

    res = supabase.table("sections").select("*").execute()

    sections = res.data

    print("Total sections:", len(sections))

    for sec in sections:

        html = sec["html_code"]

        category = detect_category(html)

        supabase.table("sections")\
            .update({"category": category})\
            .eq("id", sec["id"])\
            .execute()

        print("Updated:", category)


if __name__ == "__main__":
    clean_database()