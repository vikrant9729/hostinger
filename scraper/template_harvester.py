import requests
from bs4 import BeautifulSoup
from app.scraper.source_list import SOURCES


def collect_template_links():

    links = []

    for site in SOURCES:

        try:

            html = requests.get(site, timeout=20).text

            soup = BeautifulSoup(html, "html.parser")

            for a in soup.find_all("a"):

                href = a.get("href")

                if href and ("template" in href or "theme" in href):

                    if href.startswith("http"):
                        links.append(href)
                    else:
                        links.append(site + href)

        except:
            pass

    return list(set(links))