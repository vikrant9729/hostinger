from bs4 import BeautifulSoup


def extract_sections(html):

    soup = BeautifulSoup(html, "html.parser")

    sections = soup.find_all("section")

    return sections