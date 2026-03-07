from app.core.database import supabase


def remove_duplicate_sections():

    res = supabase.table("sections").select("*").execute()

    seen = set()

    for row in res.data:

        html = row["html_code"]

        if html in seen:

            supabase.table("sections")\
                .delete()\
                .eq("id", row["id"])\
                .execute()

        else:

            seen.add(html)


def remove_small_sections():

    res = supabase.table("sections").select("*").execute()

    for row in res.data:

        html = row["html_code"]

        if len(html) < 200:

            supabase.table("sections")\
                .delete()\
                .eq("id", row["id"])\
                .execute()


def remove_small_components():

    res = supabase.table("components").select("*").execute()

    for row in res.data:

        html = row["html_code"]

        if len(html) < 50:

            supabase.table("components")\
                .delete()\
                .eq("id", row["id"])\
                .execute()