import os
from playwright.sync_api import sync_playwright
from app.core.database import supabase

PREVIEW_FOLDER = "previews"

os.makedirs(PREVIEW_FOLDER, exist_ok=True)


def generate_preview(html, filename):

    temp_file = "temp_section.html"

    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(html)

    with sync_playwright() as p:

        browser = p.chromium.launch()

        page = browser.new_page()

        page.goto(f"file:///{os.path.abspath(temp_file)}")

        page.screenshot(path=filename, full_page=True)

        browser.close()


def process_sections():

    res = supabase.table("sections").select("*").execute()

    sections = res.data

    print("Total sections:", len(sections))

    for sec in sections:

        html = sec["html_code"]

        file_name = f"{PREVIEW_FOLDER}/{sec['id']}.png"

        try:

            generate_preview(html, file_name)

            supabase.table("sections")\
                .update({"preview_image": file_name})\
                .eq("id", sec["id"])\
                .execute()

            print("Preview created:", file_name)

        except Exception as e:

            print("Error:", e)


if __name__ == "__main__":

    process_sections()