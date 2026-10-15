import requests

from bs4 import BeautifulSoup


def analyze_mobile_friendly(url):

    try:

        response = requests.get(
            url,
            timeout=10
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        viewport = soup.find(
            "meta",
            attrs={
                "name": "viewport"
            }
        )

        if viewport:

            return {

                "status": "PASS",

                "message":
                "Mobile Viewport Found"

            }

        return {

            "status": "FAIL",

            "message":
            "Mobile Viewport Missing"

        }

    except Exception:

        return {

            "status": "FAIL",

            "message":
            "Unable To Analyze"

        }