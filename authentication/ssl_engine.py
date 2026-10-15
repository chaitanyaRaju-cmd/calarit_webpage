import ssl

import socket

from datetime import datetime


def check_ssl_certificate(url):

    try:

        hostname = (
            url.replace(
                "https://",
                ""
            )
            .replace(
                "http://",
                ""
            )
            .split("/")[0]
        )

        context = (
            ssl.create_default_context()
        )

        with socket.create_connection(
            (hostname, 443)
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=hostname
            ) as secure_sock:

                certificate = (
                    secure_sock.getpeercert()
                )

        issuer = dict(
            x[0]
            for x in certificate["issuer"]
        )

        issuer_name = issuer.get(
            "organizationName",
            "Unknown"
        )

        expiry_string = (
            certificate["notAfter"]
        )

        expiry_date = datetime.strptime(
            expiry_string,
            "%b %d %H:%M:%S %Y %Z"
        )

        remaining_days = (
            expiry_date -
            datetime.utcnow()
        ).days

        return {

            "status":
            "VALID",

            "issuer":
            issuer_name,

            "expiry_date":
            expiry_date.strftime(
                "%d-%b-%Y"
            ),

            "days_remaining":
            remaining_days
        }

    except Exception as e:

        return {

            "status":
            "INVALID",

            "issuer":
            "-",

            "expiry_date":
            "-",

            "days_remaining":
            "-",

            "error":
            str(e)
        }