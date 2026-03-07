import uuid
from bs4 import BeautifulSoup
from app.core.database import supabase


def extract_components(html):

    soup = BeautifulSoup(html, "html.parser")

    # Buttons
    buttons = soup.find_all("button")

    for b in buttons:

        data = {

        "id": str(uuid.uuid4()),
        "name": "button",
        "category": "button",
        "html_code": str(b),
        "css_code": "",
        "tags": ["button"]

        }

        supabase.table("components").insert(data).execute()


    # Forms
    forms = soup.find_all("form")

    for f in forms:

        data = {

        "id": str(uuid.uuid4()),
        "name": "form",
        "category": "form",
        "html_code": str(f),
        "css_code": "",
        "tags": ["form"]

        }

        supabase.table("components").insert(data).execute()


    # Inputs
    inputs = soup.find_all("input")

    for i in inputs:

        data = {

        "id": str(uuid.uuid4()),
        "name": "input",
        "category": "input",
        "html_code": str(i),
        "css_code": "",
        "tags": ["input"]

        }

        supabase.table("components").insert(data).execute()


    # Cards
    cards = soup.find_all("div", class_=lambda x: x and "card" in x)

    for c in cards:

        data = {

        "id": str(uuid.uuid4()),
        "name": "card",
        "category": "card",
        "html_code": str(c),
        "css_code": "",
        "tags": ["card"]

        }

        supabase.table("components").insert(data).execute()