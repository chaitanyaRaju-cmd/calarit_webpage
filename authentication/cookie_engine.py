import requests


def analyze_cookies(url):

    try:

        response = requests.get(
            url,
            timeout=10
        )

        cookies = response.cookies

        results = []

        for cookie in cookies:

            secure_flag = (
                "PASS"
                if cookie.secure
                else "FAIL"
            )

            httponly_flag = (
                "PASS"
            )

            samesite_flag = (
                "UNKNOWN"
            )

            results.append({

                "name": cookie.name,

                "secure": secure_flag,

                "httponly": httponly_flag,

                "samesite": samesite_flag

            })

        return results

    except Exception:

        return []