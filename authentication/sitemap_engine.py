import requests

from bs4 import BeautifulSoup

def analyze_sitemap(url):

    try:

        sitemap_url = (
            url.rstrip("/")
            + "/sitemap.xml"
        )

        response = requests.get(
            sitemap_url,
            timeout=10
        )

        if response.status_code != 200:

            return {

                "status": "FAIL",

                "url_count": 0,

                "message":
                "Sitemap Not Found"

            }

        soup = BeautifulSoup(
            response.content,
            "xml"
        )

        urls = soup.find_all(
            "loc"
        )

        return {

            "status": "PASS",

            "url_count":
            len(urls),

            "message":
            "Sitemap Found"

        }

    except Exception:

        return {

            "status": "FAIL",

            "url_count": 0,

            "message":
            "Sitemap Not Found"

        }