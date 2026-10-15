import socket


def analyze_ports(url):

    ports = [

        (80, "HTTP"),
        (443, "HTTPS"),
        (21, "FTP"),
        (22, "SSH")

    ]

    results = []

    try:

        host = url.replace(
            "https://",
            ""
        ).replace(
            "http://",
            ""
        ).split("/")[0]

        for port, service in ports:

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(1)

            result = sock.connect_ex(
                (host, port)
            )

            if result == 0:

                status = "OPEN"

            else:

                status = "CLOSED"

            results.append({

                "port": port,

                "service": service,

                "status": status

            })

            sock.close()

    except Exception:

        pass

    return results