import requests


def check_directory_listing(url):

    paths = [

        "/uploads/",
        "/images/",
        "/backup/",
        "/files/"

    ]

    results = []

    for path in paths:

        try:

            target_url = (
                url.rstrip("/")
                + path
            )

            response = requests.get(
                target_url,
                timeout=5
            )

            page = response.text.lower()

            if "index of" in page:

                results.append({

                    "path": path,

                    "status": "FAIL"

                })

            else:

                results.append({

                    "path": path,

                    "status": "PASS"

                })

        except Exception:

            results.append({

                "path": path,

                "status": "PASS"

            })

    return results