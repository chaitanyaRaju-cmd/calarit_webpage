import dns.resolver
from urllib.parse import urlparse


def analyze_email_security(url):

    try:

        domain = (
            urlparse(url).netloc
            .replace("www.", "")
        )

        results = []

        # SPF

        try:

            txt_records = dns.resolver.resolve(
                domain,
                "TXT"
            )

            spf_found = any(
                "v=spf1" in str(record)
                for record in txt_records
            )

            results.append({

                "name": "SPF Record",

                "status":
                "PASS" if spf_found
                else "FAIL"

            })

        except:

            results.append({

                "name": "SPF Record",

                "status": "FAIL"

            })

        # MX

        try:

            dns.resolver.resolve(
                domain,
                "MX"
            )

            results.append({

                "name": "MX Record",

                "status": "PASS"

            })

        except:

            results.append({

                "name": "MX Record",

                "status": "FAIL"

            })

        # DMARC

        try:

            dns.resolver.resolve(

                "_dmarc." + domain,

                "TXT"

            )

            results.append({

                "name": "DMARC Record",

                "status": "PASS"

            })

        except:

            results.append({

                "name": "DMARC Record",

                "status": "FAIL"

            })

        # DKIM

        try:

            dns.resolver.resolve(

                "default._domainkey."
                + domain,

                "TXT"

            )

            results.append({

                "name": "DKIM",

                "status": "PASS"

            })

        except:

            results.append({

                "name": "DKIM",

                "status": "FAIL"

            })

        return results

    except Exception:

        return [

            {

                "name": "SPF Record",

                "status": "FAIL"

            }

        ]