from bs4 import BeautifulSoup


def extract_assets(html):

    soup = BeautifulSoup(html, "html.parser")

    css = []
    js = []
    images = []

    for link in soup.find_all("link"):

        href = link.get("href")

        if href and ".css" in href:

            css.append(href)

    for script in soup.find_all("script"):

        src = script.get("src")

        if src and ".js" in src:

            js.append(src)

    for img in soup.find_all("img"):

        src = img.get("src")

        if src:

            images.append(src)

    return css, js, images  