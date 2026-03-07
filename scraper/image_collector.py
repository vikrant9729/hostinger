import uuid
from app.core.database import supabase

queries = [

"restaurant",
"startup",
"fitness",
"portfolio",
"saas",
"agency",
"ecommerce"

]

def collect_images():

    for q in queries:

        url = f"https://source.unsplash.com/1600x900/?{q}"

        supabase.table("images").insert({

        "id":str(uuid.uuid4()),
        "url":url,
        "category":q,
        "tags":[q]

        }).execute()