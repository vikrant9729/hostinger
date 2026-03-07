import random
from app.core.database import supabase

categories = [
"navbar",
"hero",
"features",
"pricing",
"gallery",
"testimonials",
"contact",
"footer"
]

def generate_section(category,i):

    html = f"""
<section style='padding:80px;text-align:center'>
<h2>{category.upper()} SECTION {i}</h2>
<p>Generated section</p>
</section>
"""

    return html


def create_sections():

    for cat in categories:

        for i in range(50):

            html = generate_section(cat,i)

            data = {

                "name":f"{cat}_{i}",

                "category":cat,

                "industry":"general",

                "style":"modern",

                "html_code":html,

                "css_code":"",

                "js_code":"",

                "preview_image":"",

                "tags":[cat]

            }

            supabase.table("sections").insert(data).execute()

            print("Created:",cat,i)


if __name__ == "__main__":

    create_sections()