import requests


def analyze_robots(url):

    try:

        robots_url = (
            url.rstrip("/")
            + "/robots.txt"
        )

        response = requests.get(
            robots_url,
            timeout=10
        )

        if response.status_code == 200:

            return {
                "status": "PASS",
                "message": "robots.txt Found",
                "url": robots_url
            }

        return {
            "status": "FAIL",
            "message": "robots.txt Not Found",
            "url": robots_url
        }

    except Exception:

        return {
            "status": "FAIL",
            "message": "Unable to Analyze robots.txt",
            "url": ""
        }