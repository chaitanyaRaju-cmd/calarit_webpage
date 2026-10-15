import requests
from bs4 import BeautifulSoup


def check_seo(url):

    results = []

    try:

        response = requests.get(
            url,
            timeout=10
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        title = soup.find("title")

        meta_description = soup.find(
            "meta",
            attrs={"name": "description"}
        )

        h1 = soup.find("h1")

        results.append({
            "name": "Title Tag",
            "status":
            "PASS" if title else "FAIL"
        })

        results.append({
            "name": "Meta Description",
            "status":
            "PASS" if meta_description else "FAIL"
        })

        results.append({
            "name": "H1 Tag",
            "status":
            "PASS" if h1 else "FAIL"
        })

        return results

    except Exception:

        return [{
            "name": "SEO Scan",
            "status": "FAIL"
        }]