import requests


def analyze_sensitive_files(url):

    sensitive_paths = [

        "/.env",
        "/.git",
        "/backup.zip",
        "/database.sql",
        "/config.php"

    ]

    results = []

    try:

        for path in sensitive_paths:

            target_url = (
                url.rstrip("/")
                + path
            )

            try:

                response = requests.get(
                    target_url,
                    timeout=5
                )

                if response.status_code == 200:

                    results.append({

                        "file": path,

                        "status": "FAIL"

                    })

                else:

                    results.append({

                        "file": path,

                        "status": "PASS"

                    })

            except:

                results.append({

                    "file": path,

                    "status": "PASS"

                })

        return results

    except Exception:

        return []