import requests


def download_template(url):

    try:

        html = requests.get(url, timeout=20).text

        return html

    except:

        return None