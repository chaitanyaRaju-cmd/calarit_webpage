import requests

from bs4 import BeautifulSoup

from urllib.parse import (
    urljoin
)


def check_broken_links(url):

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

        links = soup.find_all("a")

        checked = set()

        for link in links:

            href = link.get("href")

            if not href:

                continue

            full_url = urljoin(
                url,
                href
            )

            if full_url in checked:

                continue

            checked.add(
                full_url
            )

            try:

                r = requests.get(
                    full_url,
                    timeout=5
                )

                status = (
                    "PASS"
                    if r.status_code < 400
                    else "FAIL"
                )

                results.append({
                    "url": full_url,
                    "status": status,
                    "code": r.status_code
                })

            except Exception:

                results.append({
                    "url": full_url,
                    "status": "FAIL",
                    "code": "ERROR"
                })

        return results

    except Exception:

        return []