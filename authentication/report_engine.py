from datetime import datetime


def build_executive_summary(
    website_url,
    section_scores,
    https_result,
    ssl_result,
    issues_summary
):

    overall_score = section_scores["overall_score"]
    risk_level = section_scores["risk_level"]

    if overall_score >= 90:
        assessment = (
            "The website demonstrates an excellent security posture with strong "
            "configuration and minimal risks."
        )

    elif overall_score >= 75:
        assessment = (
            "The website demonstrates a generally secure configuration. "
            "Several improvements are recommended to further strengthen "
            "security and performance."
        )

    elif overall_score >= 50:
        assessment = (
            "The website contains several findings that should be addressed "
            "to improve security and user experience."
        )

    else:
        assessment = (
            "The website contains critical issues that require immediate attention."
        )

    key_findings = []

    if https_result["status"] == "PASS":
        key_findings.append("HTTPS is properly configured.")
    else:
        key_findings.append("HTTPS is not configured correctly.")

    if ssl_result["status"] == "PASS":
        key_findings.append("SSL certificate is valid.")
    else:
        key_findings.append("SSL certificate requires attention.")

    if issues_summary.get("critical", 0) > 0:
       key_findings.append(
        f'{issues_summary["critical"]} Critical Issue(s) Detected'
    )
       
    if issues_summary.get("high", 0) > 0:
       key_findings.append(
        f'{issues_summary["high"]} High Severity Issue(s) Detected'
    )

    if issues_summary.get("medium", 0) > 0:
        key_findings.append(
        f'{issues_summary["medium"]} Medium Severity Issue(s) Detected'
    )

    if issues_summary.get("low", 0) > 0:
       key_findings.append(
        f'{issues_summary["low"]} Low Severity Issue(s) Detected'
    )

    return {

        "website": website_url,

        "scan_date": datetime.now().strftime("%d %B %Y"),

        "overall_score": overall_score,

        "risk_level": risk_level,

        "assessment": assessment,

        "key_findings": key_findings

    }

def build_security_findings(security_results):

    findings = []

    for item in security_results:

        name = item["name"]
        status = item["status"]

        if name == "Content-Security-Policy":

            findings.append({

                "title": "Content-Security-Policy Header",

                "status":
                "Configured" if status == "PASS" else "Not Configured",

                "meaning":
                "Defines which content sources browsers are allowed to load.",

                "impact":
                "Without this header, attackers may exploit Cross-Site Scripting (XSS) vulnerabilities more easily.",

                "recommendation":
                "Configure a Content-Security-Policy header with trusted content sources.",

                "severity":
                "High" if status == "FAIL" else "Low"
            })

        elif name == "X-Frame-Options":

           findings.append({

        "title": "X-Frame-Options Header",

        "status":
        "Configured" if status == "PASS" else "Not Configured",

        "meaning":
        "Prevents the website from being embedded inside unauthorized frames or iframes.",

        "impact":
        "Missing this header may allow Clickjacking attacks that trick users into performing unintended actions.",

        "recommendation":
        "Configure the X-Frame-Options header as DENY or SAMEORIGIN.",

        "severity":
        "High" if status == "FAIL" else "Low"
    })

        elif name == "Referrer-Policy":

            findings.append({

                "title": "Referrer-Policy Header",

                "status":
                "Configured" if status == "PASS" else "Not Configured",

                "meaning":
                "Controls how much referral information browsers share with external websites.",

                "impact":
                "Sensitive URL information may be exposed.",

                "recommendation":
                "Configure strict-origin-when-cross-origin.",

                "severity":
                "Medium" if status == "FAIL" else "Low"
            })

        elif name == "X-Content-Type-Options":

            findings.append({

        "title": "X-Content-Type-Options Header",

        "status":
        "Configured" if status == "PASS" else "Not Configured",

        "meaning":
        "Prevents browsers from MIME-sniffing a response away from its declared content type.",

        "impact":
        "Without this header, browsers may incorrectly interpret files, increasing certain security risks.",

        "recommendation":
        "Configure the X-Content-Type-Options header with the value 'nosniff'.",

        "severity":
        "Medium" if status == "FAIL" else "Low"
    })

        elif name == "Strict-Transport-Security":

         findings.append({

        "title": "Strict-Transport-Security Header",

        "status":
        "Configured" if status == "PASS" else "Not Configured",

        "meaning":
        "Forces browsers to communicate with the website only over HTTPS.",

        "impact":
        "Without HSTS, users may be vulnerable to protocol downgrade and man-in-the-middle attacks.",

        "recommendation":
        "Enable the Strict-Transport-Security header with an appropriate max-age value.",

       "severity":
       "High" if status == "FAIL" else "Low"

    })
         
        elif name == "HTTPS":

          findings.append({

        "title": "HTTPS Configuration",

        "status":
        "Enabled" if status == "PASS" else "Disabled",

        "meaning":
        "HTTPS encrypts communication between users and the website.",

        "impact":
        "Without HTTPS, sensitive information can be intercepted during transmission.",

        "recommendation":
        "Use HTTPS across the entire website and redirect all HTTP requests to HTTPS.",

       "severity":
       "Critical" if status == "FAIL" else "Low"
    })

        

        

    return findings

def build_availability_report(availability_result):

    status = availability_result["status"]
    http_code = availability_result["code"]

    if status == "PASS":

        reason = (
            "The website responded successfully to the request, confirming that "
            "the web server is accessible and operational."
        )

        impact = (
            "Users can access the website without interruption, resulting in "
            "good availability and a better user experience."
        )

        recommendation = (
            "No immediate action is required. Continue monitoring the website "
            "to ensure consistent availability."
        )

    else:

        reason = (
            "The website did not respond successfully to the request."
        )

        impact = (
            "Users may be unable to access the website, which can lead to "
            "service disruption and potential business impact."
        )

        recommendation = (
            "Verify the web server, hosting service, DNS configuration, "
            "or network connectivity."
        )

    return {

        "meaning":
        (
            "Website Availability determines whether the website is reachable "
            "and capable of responding to user requests over the internet."
        ),

        "status": status,

        "http_code": http_code,

        "reason": reason,

        "impact": impact,

        "recommendation": recommendation

    }

def build_https_report(https_result):

    status = https_result["status"]
    message = https_result["message"]

    if status == "PASS":

        reason = (
            "The website is using HTTPS, ensuring that communication between "
            "the user's browser and the server is encrypted."
        )

        impact = (
            "Sensitive information such as login credentials and personal "
            "data is protected against interception."
        )

        recommendation = (
            "No action is required. Continue renewing SSL certificates "
            "before they expire."
        )

    else:

        reason = (
            "The website is not using a secure HTTPS connection."
        )

        impact = (
            "Data transmitted between users and the website may be exposed "
            "to attackers."
        )

        recommendation = (
            "Install a valid SSL certificate and redirect all HTTP traffic "
            "to HTTPS."
        )

    return {

        "meaning":
        (
            "HTTPS encrypts communication between users and the website, "
            "protecting sensitive information during transmission."
        ),

        "status": status,

        "message": message,

        "reason": reason,

        "impact": impact,

        "recommendation": recommendation

    }

def build_ssl_report(ssl_result):

    status = ssl_result["status"]

    issuer = ssl_result["issuer"]

    expiry_date = ssl_result["expiry_date"]

    days_remaining = ssl_result["days_remaining"]

    if status == "VALID":

        reason = (
            "The website is using a valid SSL certificate issued by a trusted Certificate Authority."
        )

        impact = (
            "User data transmitted between the browser and the website is encrypted and trusted."
        )

        recommendation = (
            "Continue monitoring the certificate and renew it before it expires."
        )

    else:

        reason = (
            "The SSL certificate is invalid or could not be verified."
        )

        impact = (
            "Visitors may receive browser security warnings, reducing trust and potentially preventing access."
        )

        recommendation = (
            "Install or renew a valid SSL certificate immediately."
        )

    return {

        "meaning":
        (
            "An SSL Certificate authenticates a website and enables encrypted communication between the browser and the server."
        ),

        "status": status,

        "issuer": issuer,

        "expiry_date": expiry_date,

        "days_remaining": days_remaining,

        "reason": reason,

        "impact": impact,

        "recommendation": recommendation

    }

def build_cookie_report(cookie_results):

    report = []

    for cookie in cookie_results:

        if (

             cookie["secure"] == "PASS"

             and

             cookie["httponly"] == "PASS"

             and

             cookie["samesite"] == "PASS"

        ):

            impact = (
                "The cookie is transmitted only over encrypted HTTPS connections, reducing the risk of interception."
            )

            recommendation = (
                "No action is required."
            )

        else:

            missing_attributes = []

            if cookie["secure"] != "PASS":
               missing_attributes.append("Secure")

            if cookie["httponly"] != "PASS":
               missing_attributes.append("HttpOnly")
            
            if cookie["samesite"] != "PASS":
               missing_attributes.append("SameSite")

            impact = (
               "The cookie is missing the following security attribute(s): "
               + ", ".join(missing_attributes)
               + ". This may increase the risk of session hijacking, cross-site scripting (XSS), or cross-site request forgery (CSRF) attacks."
            )

            recommendation = (
                "Configure the following cookie attribute(s): "
                + ", ".join(missing_attributes)
                + " to improve cookie security."
            )

        report.append({

            "name": cookie["name"],

            "meaning":
            (
                "Cookies store information in the user's browser to maintain sessions and preferences."
            ),

            "secure": cookie["secure"],

            "httponly": cookie["httponly"],

            "samesite": cookie["samesite"],

            "impact": impact,

            "recommendation": recommendation

        })

    return report

def build_broken_link_report(broken_links):

    report = []

    for link in broken_links:

        if link["status"] == "PASS":

            impact = (
                "The link is accessible and provides a good user experience."
            )

            recommendation = (
                "No action is required."
            )

        else:

            impact = (
                "Broken links can frustrate users, reduce website credibility, and negatively affect search engine rankings."
            )

            recommendation = (
                "Update, repair, or remove the broken link so users can access the intended resource."
            )

        report.append({

            "meaning":
            (
                "Broken Link Analysis verifies whether hyperlinks on the website lead to valid and accessible resources."
            ),

            "url": link["url"],

            "status": link["status"],

            "http_code": link["code"],

            "impact": impact,

            "recommendation": recommendation

        })

    return report

def build_robots_report(robots_result):

    if robots_result["status"] == "PASS":

        impact = (
            "Search engine crawlers can easily discover website crawling rules, improving indexing and crawl management."
        )

        recommendation = (
            "No action is required."
        )

        reason = (
            "The website provides a valid robots.txt file that is accessible."
        )

    else:

        impact = (
            "Search engines may not receive crawling instructions, which can affect indexing and visibility."
        )

        recommendation = (
            "Create and maintain a valid robots.txt file in the website root directory."
        )

        reason = (
            "No accessible robots.txt file was found."
        )

    return {

        "meaning":
        (
            "The robots.txt file tells search engine crawlers which parts of a website they are allowed or not allowed to crawl."
        ),

        "status":
        robots_result["status"],

        "url":
        robots_result["url"],

        "reason":
        reason,

        "impact":
        impact,

        "recommendation":
        recommendation

    }
def build_sitemap_report(sitemap_result):

    if sitemap_result["status"] == "PASS":

        reason = (
            "A valid sitemap.xml file was found and successfully parsed."
        )

        impact = (
            "Search engines can efficiently discover and index website pages, improving SEO visibility."
        )

        recommendation = (
            "No action is required."
        )

    else:

        reason = (
            "No accessible sitemap.xml file was found."
        )

        impact = (
            "Search engines may take longer to discover website pages, reducing indexing efficiency."
        )

        recommendation = (
            "Create and submit a valid sitemap.xml file."
        )

    return {

        "meaning":
        (
            "A sitemap.xml file provides search engines with a structured list of important pages available on the website."
        ),

        "status":
        sitemap_result["status"],

        "url_count":
        sitemap_result["url_count"],

        "message":
        sitemap_result["message"],

        "reason":
        reason,

        "impact":
        impact,

        "recommendation":
        recommendation

    }
def build_mobile_report(mobile_result):

    if mobile_result["status"] == "PASS":

        reason = (
            "The website satisfies the essential mobile-friendly checks and can "
            "be used comfortably on smartphones and tablets."
        )

        impact = (
            "Visitors using mobile devices will have a better browsing "
            "experience, improving usability and engagement."
        )

        recommendation = (
            "Continue maintaining responsive layouts and regularly test on "
            "different mobile devices."
        )

    else:

        reason = (
            "The website failed one or more mobile usability checks."
        )

        impact = (
            "Users may experience layout issues, difficult navigation, or poor "
            "readability on smaller screens."
        )

        recommendation = (
            "Implement responsive web design using CSS media queries and "
            "optimize the website for mobile devices."
        )

    return {

        "status": mobile_result["status"],

        "meaning":
        "A mobile-friendly website automatically adapts its layout and content to different screen sizes, providing a better experience on smartphones and tablets.",

        "reason": reason,

        "impact": impact,

        "recommendation": recommendation

    }
def build_sensitive_files_report(sensitive_files_result):

    exposed_files = [

        item["file"]

        for item in sensitive_files_result

        if item["status"] == "FAIL"

    ]

    files_found = len(exposed_files)

    if files_found == 0:

        status = "PASS"

        reason = (
            "No publicly accessible sensitive files were detected during the scan."
        )

        impact = (
            "Sensitive configuration files are protected, reducing the risk of information disclosure."
        )

        recommendation = (
            "Continue restricting public access to configuration, backup and administrative files."
        )

    else:

        status = "FAIL"

        reason = (
            "One or more sensitive files are publicly accessible."
        )

        impact = (
            "Attackers may obtain confidential information such as credentials, configuration files or backups."
        )

        recommendation = (
            "Immediately restrict access to these files and remove them from public access."
        )

    return {

        "status": status,

        "files_found": files_found,

        "exposed_files": exposed_files,

        "meaning":
        "Sensitive files include environment files, backups, database dumps and configuration files that should never be publicly accessible.",

        "reason": reason,

        "impact": impact,

        "recommendation": recommendation

    }
def build_technology_report(technology_results):

    technologies = technology_results.get(
        "technologies",
        []
    )

    server = technology_results.get(
        "server",
        "Unknown"
    )

    framework = technology_results.get(
        "framework",
        "Unknown"
    )

    language = technology_results.get(
        "language",
        "Unknown"
    )

    detected = [

        tech

        for tech in technologies

        if tech != "Unknown"
        and tech != "Unable To Detect"

    ]

    technology_count = len(detected)

    if technology_count > 0:

        status = "PASS"

        reason = (
            "The scan successfully identified the technologies powering the website."
        )

        impact = (
            "Knowing the server, framework and programming language helps maintain software, identify outdated components and improve security management."
        )

        recommendation = (
            "Keep all detected technologies updated with the latest stable security patches."
        )

    else:

        status = "FAIL"

        reason = (
            "The scan could not reliably identify the technologies used by the website."
        )

        impact = (
            "Technology inventory could not be established, making maintenance and vulnerability tracking more difficult."
        )

        recommendation = (
            "Verify website accessibility and rerun the technology detection scan."
        )

    return {

        "status": status,

        "technology_count": technology_count,

        "technologies": detected,

        "server": server,

        "framework": framework,

        "language": language,

        "meaning":
        "Technology Detection identifies the server software, web framework, programming language and third-party technologies used by the website.",

        "reason": reason,

        "impact": impact,

        "recommendation": recommendation

    }
def build_directory_listing_report(results):

    vulnerable = any(
        item["status"] == "FAIL"
        for item in results
    )

    if vulnerable:

        status = "FAIL"

        reason = (
            "One or more directories appear to allow public listing."
        )

        impact = (
            "Attackers may discover sensitive files or application structure."
        )

        recommendation = (
            "Disable directory listing in the web server configuration."
        )

    else:

        status = "PASS"

        reason = (
            "No publicly accessible directory listing was detected."
        )

        impact = (
            "Website directories are protected from unauthorized browsing."
        )

        recommendation = (
            "No action is required. Continue restricting directory indexing."
        )

    return {

        "meaning":
        "Directory Listing determines whether website folders can be browsed directly by visitors.",

        "status": status,

        "directories": results,

        "reason": reason,

        "impact": impact,

        "recommendation": recommendation

    }
def build_performance_report(result):

    status = result.get("status", "FAIL")
    score = result.get("score", 0)
    load_time = result.get("load_time", 0)
    page_size = result.get("page_size", 0)
    images = result.get("images", 0)
    scripts = result.get("scripts", 0)

    if status == "PASS":

        reason = (
            "The website completed the performance scan successfully."
        )

        impact = (
            "Good website performance improves user experience and search engine ranking."
        )

        recommendation = (
            "Continue monitoring performance and optimize large assets whenever necessary."
        )

    else:

        reason = (
            "The website performance scan indicates performance issues."
        )

        impact = (
            "Slow loading pages may reduce user satisfaction and increase bounce rates."
        )

        recommendation = (
            "Optimize images, CSS, JavaScript and enable browser caching."
        )

    return {

        "meaning":
        "Performance Analysis measures the loading speed and efficiency of a website.",

        "status":
        status,

        "score":
        score,

        "load_time":
        load_time,

        "page_size":
        page_size,

        "images":
        images,

        "scripts":
        scripts,

        "reason":
        reason,

        "impact":
        impact,

        "recommendation":
        recommendation

    }
def build_accessibility_report(results):

    passed = len([
        x for x in results
        if x["status"] == "PASS"
    ])

    total = len(results)

    score = round(
        (passed / total) * 100
    ) if total else 0

    if score >= 80:

        status = "PASS"

        reason = (
            "Most accessibility checks passed successfully."
        )

        impact = (
            "The website is accessible for most users, including those using assistive technologies."
        )

        recommendation = (
            "Continue following accessibility best practices and periodically audit the website."
        )

    elif score >= 60:

        status = "WARNING"

        reason = (
            "Some accessibility issues were detected."
        )

        impact = (
            "Certain users may experience usability problems."
        )

        recommendation = (
            "Fix the failed accessibility checks to improve usability."
        )

    else:

        status = "FAIL"

        reason = (
            "Multiple accessibility issues were detected."
        )

        impact = (
            "Users with disabilities may experience significant difficulties using the website."
        )

        recommendation = (
            "Implement accessibility standards such as WCAG 2.1."
        )

    return {

        "meaning":
        "Accessibility Analysis evaluates whether a website follows accessibility best practices for all users.",

        "status":
        status,

        "score":
        score,

        "passed":
        passed,

        "total":
        total,

        "reason":
        reason,

        "impact":
        impact,

        "recommendation":
        recommendation

    }
def build_domain_info_report(result):

    status = result.get(
        "status",
        "FAIL"
    )

    if status == "PASS":

        reason = (
            "The domain registration information was successfully retrieved."
        )

        impact = (
            "Domain ownership and expiration details help monitor domain validity and reduce the risk of unexpected expiration."
        )

        recommendation = (
            "Monitor the domain expiration date and renew it before expiry."
        )

    else:

        reason = (
            "Unable to retrieve domain registration information."
        )

        impact = (
            "Missing domain information may prevent administrators from monitoring domain ownership and renewal."
        )

        recommendation = (
            "Verify the domain registration details and WHOIS availability."
        )

    return {

        "meaning":
        "Domain Information Analysis retrieves WHOIS information such as domain registrar, creation date, expiration date and remaining validity.",

        "status":
        status,

        "domain":
        result.get(
            "domain",
            "Unknown"
        ),

        "registrar":
        result.get(
            "registrar",
            "Unknown"
        ),

        "created":
        result.get(
            "created",
            "N/A"
        ),

        "expires":
        result.get(
            "expires",
            "N/A"
        ),

        "days_remaining":
        result.get(
            "days_remaining",
            0
        ),

        "reason":
        reason,

        "impact":
        impact,

        "recommendation":
        recommendation

    }
def build_email_security_report(results):

    passed = len([
        x for x in results
        if x["status"] == "PASS"
    ])

    total = len(results)

    score = round((passed / total) * 100) if total else 0

    if score >= 80:

        status = "PASS"

        reason = (
            "Email authentication records are properly configured."
        )

        impact = (
            "Email spoofing and phishing risks are minimized."
        )

        recommendation = (
            "Continue monitoring SPF, MX, DKIM and DMARC records."
        )

    elif score >= 60:

        status = "WARNING"

        reason = (
            "Some email security records are missing."
        )

        impact = (
            "Email spoofing protection is only partially enabled."
        )

        recommendation = (
            "Configure the missing email security records."
        )

    else:

        status = "FAIL"

        reason = (
            "Most email security records are missing."
        )

        impact = (
            "The domain is vulnerable to spoofing and phishing attacks."
        )

        recommendation = (
            "Implement SPF, MX, DKIM and DMARC records."
        )

    return {

        "meaning":
        "Email Security Analysis verifies whether the domain is protected using SPF, MX, DKIM and DMARC records.",

        "status":
        status,

        "score":
        score,

        "passed":
        passed,

        "total":
        total,

        "reason":
        reason,

        "impact":
        impact,

        "recommendation":
        recommendation

    }
def build_ports_report(results):

    open_ports = len([
        x
        for x in results
        if x["status"] == "OPEN"
    ])

    total = len(results)

    if open_ports == 0:

        status = "PASS"

        reason = (
            "No monitored ports are publicly accessible."
        )

        impact = (
            "The server exposes minimal network services."
        )

        recommendation = (
            "Continue restricting unnecessary network ports."
        )

    elif open_ports <= 2:

        status = "WARNING"

        reason = (
            "Only a few monitored ports are open."
        )

        impact = (
            "Some services are publicly accessible."
        )

        recommendation = (
            "Verify that only required services remain open."
        )

    else:

        status = "FAIL"

        reason = (
            "Multiple monitored ports are publicly accessible."
        )

        impact = (
            "Open ports may increase the attack surface."
        )

        recommendation = (
            "Close unused services and restrict exposed ports."
        )

    return {

        "meaning":
        "Open Ports Analysis identifies network ports that are accessible from the internet.",

        "status":
        status,

        "open_ports":
        open_ports,

        "total":
        total,

        "reason":
        reason,

        "impact":
        impact,

        "recommendation":
        recommendation

    }

def build_final_conclusion(
    website_url,
    section_scores,
    issues_summary
):

    overall = section_scores.get(
        "overall_score",
        0
    )

    if overall >= 90:

        verdict = "EXCELLENT"

    elif overall >= 75:

        verdict = "GOOD"

    elif overall >= 60:

        verdict = "FAIR"

    else:

        verdict = "POOR"

    # Dynamic Recommendation

    if issues_summary.get("critical", 0) > 0:

        recommendation = (
            "Immediately resolve all Critical security issues before deploying the website."
        )

    elif issues_summary.get("medium", 0) > 0:

        recommendation = (
            "Resolve Medium severity issues to strengthen the website's overall security posture."
        )

    elif issues_summary.get("low", 0) > 0:

        recommendation = (
            "Address Low severity findings during routine maintenance to improve website quality."
        )

    else:

        recommendation = (
            "No significant issues were detected. Continue periodic security assessments and monitoring."
        )

    # Dynamic Summary

    summary = (
        f"The website achieved an overall security score of "
        f"{overall}/100 and is rated as {verdict}. "
        f"The audit identified "
        f"{issues_summary.get('critical', 0)} Critical, "
        f"{issues_summary.get('medium', 0)} Medium and "
        f"{issues_summary.get('low', 0)} Low severity issue(s). "
        "The assessment covered security, SEO, accessibility, "
        "performance, technology, domain configuration, "
        "email security and network exposure."
    )

    return {

        "website": website_url,

        "overall_score": overall,

        "verdict": verdict,

        "critical":
        issues_summary.get(
            "critical",
            0
        ),

        "medium":
        issues_summary.get(
            "medium",
            0
        ),

        "low":
        issues_summary.get(
            "low",
            0
        ),

        "summary": summary,

        "recommendation": recommendation

    }