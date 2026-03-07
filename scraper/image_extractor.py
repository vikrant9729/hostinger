import uuid
from bs4 import BeautifulSoup
from app.core.database import supabase


def extract_images(html):

    soup = BeautifulSoup(html,"html.parser")

    imgs = soup.find_all("img")

    for img in imgs:

        src = img.get("src")

        if src:

            supabase.table("images").insert({

            "id":str(uuid.uuid4()),
            "url":src,
            "category":"template",
            "tags":["auto"]

            }).execute()