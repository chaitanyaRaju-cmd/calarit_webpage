import requests

from bs4 import BeautifulSoup


def detect_technologies(url):

    technologies = []

    try:

        response = requests.get(
            url,
            timeout=10
        )

        html = response.text.lower()

        headers = response.headers

        # React

        if "react" in html:

            technologies.append(
                "React"
            )

        # Angular

        if "ng-app" in html:

            technologies.append(
                "Angular"
            )

        # Vue

        if "vue" in html:

            technologies.append(
                "Vue.js"
            )

        # Bootstrap

        if "bootstrap" in html:

            technologies.append(
                "Bootstrap"
            )

        # jQuery

        if "jquery" in html:

            technologies.append(
                "jQuery"
            )

        # WordPress

        if "wp-content" in html:

            technologies.append(
                "WordPress"
            )

        # Google Analytics

        if "google-analytics" in html:

            technologies.append(
                "Google Analytics"
            )

        # Cloudflare

        if (
            "cloudflare"
            in str(headers).lower()
        ):

            technologies.append(
                "Cloudflare"
            )

        if not technologies:

            technologies.append(
                "Unknown"
            )

        server = headers.get("Server", "Not Detected")

        framework = "Unknown"

        if "React" in technologies:
         framework = "React"

        elif "Angular" in technologies:
         framework = "Angular"

        elif "Vue.js" in technologies:
         framework = "Vue.js"

        elif "Bootstrap" in technologies:
         framework = "Bootstrap"

        elif "WordPress" in technologies:
         framework = "WordPress"

        language = "Not Detected"

        powered_by = headers.get("X-Powered-By", "").lower()

        if "php" in powered_by:
         language = "PHP"

        elif "asp.net" in powered_by:
         language = "ASP.NET"
        elif "express" in powered_by or "node" in powered_by:
         language = "Node.js"

        return {

    "technologies": technologies,

    "server": server,

    "framework": framework,

    "language": language

}


    except Exception:

        return {

    "technologies": ["Unable To Detect"],

    "server": "Unable To Detect",

    "framework": "Unable To Detect",

    "language": "Unable To Detect"

}