import requests

def check_https(url):

    try:

        if not url.startswith("https://"):

            return {
                "status": "FAIL",
                "message": "Not Using HTTPS"
            }

        response = requests.get(
            url,
            timeout=10,
            verify=True
        )

        return {
            "status": "PASS",
            "message": "Valid SSL Certificate"
        }

    except requests.exceptions.SSLError:

        return {
            "status": "FAIL",
            "message": "Invalid SSL Certificate"
        }

    except Exception as e:

        return {
            "status": "FAIL",
            "message": str(e)
        }
def check_availability(url):

    try:

        response = requests.get(
            url,
            timeout=10
        )

        if response.status_code < 400:

            return {
                "status": "PASS",
                "code": response.status_code
            }

        return {
            "status": "FAIL",
            "code": response.status_code
        }

    except Exception:

        return {
            "status": "FAIL",
            "code": "No Response"
        }