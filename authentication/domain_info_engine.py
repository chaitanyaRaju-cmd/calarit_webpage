import whois

from datetime import datetime, timezone


def analyze_domain_info(url):

    try:

        domain = (
            url.replace("https://", "")
               .replace("http://", "")
               .split("/")[0]
        )

        data = whois.whois(domain)

        creation_date = data.creation_date
        expiration_date = data.expiration_date

        if isinstance(
            creation_date,
            list
        ):
            creation_date = creation_date[0]

        if isinstance(
            expiration_date,
            list
        ):
            expiration_date = expiration_date[0]

        if expiration_date.tzinfo is None:

            expiration_date = (
            expiration_date.replace(
            tzinfo=timezone.utc
        )
    )

        days_remaining = (
        expiration_date -
        datetime.now(
        timezone.utc
    )
).days

        return {

            "status": "PASS",

            "domain": domain,

            "registrar":
            str(data.registrar),

            "created":
            creation_date.strftime(
                "%d-%b-%Y"
            ),

            "expires":
            expiration_date.strftime(
                "%d-%b-%Y"
            ),

            "days_remaining":
            days_remaining

        }

    except Exception as e:

        print(
             "DOMAIN ERROR:",
              str(e)
    )

        return {

            "status": "FAIL",

            "domain": "Unknown",

            "registrar": "Unknown",

            "created": "N/A",

            "expires": "N/A",

            "days_remaining": 0

        }