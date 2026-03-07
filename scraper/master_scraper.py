from app.scraper.template_harvester import collect_template_links
from app.scraper.template_downloader import download_template
from app.scraper.asset_extractor import extract_assets
from app.scraper.section_extractor import extract_sections


def run_scraper():

    links = collect_template_links()

    for link in links:

        html = download_template(link)

        if not html:
            continue

        css, js, images = extract_assets(html)

        sections = extract_sections(html)

        print("Template:", link)
        print("CSS:", len(css))
        print("JS:", len(js))
        print("Images:", len(images))
        print("Sections:", len(sections))
        print("-----------")


if __name__ == "__main__":

    run_scraper()