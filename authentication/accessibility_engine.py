import requests

from bs4 import BeautifulSoup


def analyze_accessibility(url):

    try:

        response = requests.get(
            url,
            timeout=10
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        results = []

        # ALT Tags

        images = soup.find_all(
            "img"
        )

        missing_alt = 0

        for img in images:

            if not img.get("alt"):

                missing_alt += 1

        results.append({

            "name":
            "Image ALT Tags",

            "status":
            "PASS"
            if missing_alt == 0
            else "FAIL"

        })

        # Language Tag

        html_tag = soup.find("html")

        results.append({

            "name":
            "Language Tag",

            "status":
            "PASS"
            if html_tag
            and html_tag.get("lang")
            else "FAIL"

        })

        # Form Labels

        forms = soup.find_all(
            "input"
        )

        labels = soup.find_all(
            "label"
        )

        results.append({

            "name":
            "Form Labels",

            "status":
            "PASS"
            if len(labels) >= len(forms)
            else "FAIL"

        })

        # Button Text

        buttons = soup.find_all(
            "button"
        )

        missing_text = 0

        for button in buttons:

            if not button.text.strip():

                missing_text += 1

        results.append({

            "name":
            "Button Text",

            "status":
            "PASS"
            if missing_text == 0
            else "FAIL"

        })

        return results

    except Exception:

        return [

            {
                "name":
                "Accessibility",

                "status":
                "FAIL"
            }

        ]