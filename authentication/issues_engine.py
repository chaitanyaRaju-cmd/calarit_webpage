def calculate_issues(
    security_results,
    seo_results,
    robots_result,
    sensitive_files_result,
    directory_results,
    accessibility_results,
    domain_info_result,
    email_security_results,
    ports_results,
):

    critical = 0
    high = 0
    medium = 0
    low = 0

    # ==========================
    # Security Headers
    # ==========================
    for item in security_results:

        if item["status"] == "FAIL":

            if item["name"] in [
                "Content-Security-Policy",
                "Strict-Transport-Security"
            ]:
                high += 1

            elif item["name"] in [
                "X-Frame-Options",
                "X-Content-Type-Options",
                "Referrer-Policy"
            ]:
                medium += 1

            else:
                low += 1

    # ==========================
    # SEO
    # ==========================
    for item in seo_results:

        if item["status"] == "FAIL":
            medium += 1

    # ==========================
    # Robots.txt
    # ==========================
    if robots_result["status"] == "FAIL":
        low += 1

    # ==========================
    # Sensitive Files
    # ==========================
    for item in sensitive_files_result:

        if item["status"] == "FAIL":
            critical += 1

    # ==========================
    # Directory Enumeration
    # ==========================
    for item in directory_results:

        if item["status"] == "FAIL":
            high += 1

    # ==========================
    # Accessibility
    # ==========================
    for item in accessibility_results:

        if item["status"] == "FAIL":
            low += 1

    # ==========================
    # Domain Expiry
    # ==========================
    if domain_info_result["days_remaining"] < 30:
        critical += 1

    elif domain_info_result["days_remaining"] < 90:
        high += 1

    # ==========================
    # Email Security
    # ==========================
    for item in email_security_results:

        if item["status"] == "FAIL":

            if item["name"] == "DMARC":
                high += 1
            else:
                medium += 1

    # ==========================
    # Open Ports
    # ==========================
    for item in ports_results:

        if item["status"] == "OPEN":

            if item["port"] in [21, 23]:
                high += 1

            elif item["port"] not in [80, 443]:
                medium += 1

    return {

        "critical": critical,

        "high": high,

        "medium": medium,

        "low": low

    }