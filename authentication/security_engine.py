import requests


def check_security_headers(url):

    results = []

    try:

        response = requests.get(
            url,
            timeout=10
        )

        headers = response.headers

        security_checks = {

            "HTTPS":
            url.startswith("https://"),

            "X-Frame-Options":
            "X-Frame-Options" in headers,

            "X-Content-Type-Options":
            "X-Content-Type-Options" in headers,

            "Content-Security-Policy":
            "Content-Security-Policy" in headers,

            "Strict-Transport-Security":
            "Strict-Transport-Security" in headers,

            "Referrer-Policy":
            "Referrer-Policy" in headers

        }

        for check, status in security_checks.items():

            results.append({

                "name": check,

                "status":
                "PASS" if status else "FAIL"

            })

        return results

    except Exception:

        return [{
            "name": "Security Scan",
            "status": "FAIL"
        }]