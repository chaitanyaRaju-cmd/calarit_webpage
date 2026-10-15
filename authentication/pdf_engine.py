from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib import colors

from datetime import datetime

import os

def cell(text, styles):
    """
    Returns a Paragraph for automatic word wrapping
    inside ReportLab tables.
    """

    if text is None:
        text = ""

    return Paragraph(
        str(text),
        styles["BodyText"]
    )

def generate_pdf_report(
    pdf_path,
    website_url,
    screenshot_path,
    executive_summary,
    availability_report,
    https_report,
    ssl_report,
    cookie_report,
    security_findings,
    broken_link_report,
    robots_report,
    sitemap_report,
    mobile_report,
    sensitive_files_report,
    technology_report,
    directory_listing_report,
    performance_report,
    accessibility_report,
    domain_info_report,
    email_security_report,
    ports_report,
    final_conclusion
):
    
    doc = SimpleDocTemplate(
        pdf_path
    )

    styles = getSampleStyleSheet()

    content = []

# ==========================================================
# CALARIT WEBSITE TESTING REPORT
# ==========================================================

    content.append(
    Paragraph(
        "CALARIT Website Testing Report",
        styles["Title"]
    )
)

    content.append(
    Spacer(1, 20)
)

    content.append(
    Paragraph(
        f"<b>Website:</b> {executive_summary['website']}",
        styles["BodyText"]
    )
)

    content.append(
    Paragraph(
        f"<b>Scan Date:</b> {executive_summary['scan_date']}",
        styles["BodyText"]
    )
)

    content.append(
    Spacer(1, 20)
)

# ==========================================================
# WEBSITE SCREENSHOT
# ==========================================================

    if screenshot_path:

        content.append(
        Paragraph(
            "Website Screenshot",
            styles["Heading2"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    content.append(
        Image(
            screenshot_path,
            width=420,
            height=230
        )
    )

    content.append(
        Spacer(1, 20)
    )

# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

    content.append(
    Paragraph(
        "Executive Summary",
        styles["Heading1"]
    )
)

    content.append(
    Spacer(1, 10)
)

    content.append(
    Paragraph(
        f"<b>Overall Score:</b> {executive_summary['overall_score']}/100",
        styles["BodyText"]
    )
)

    content.append(
    Paragraph(
        f"<b>Risk Level:</b> {executive_summary['risk_level']}",
        styles["BodyText"]
    )
)

    content.append(
    Spacer(1, 10)
)

    content.append(
    Paragraph(
        "<b>Assessment</b>",
        styles["Heading2"]
    )
)

    content.append(
    Paragraph(
        executive_summary["assessment"],
        styles["BodyText"]
    )
)

    content.append(
    Spacer(1, 10)
)

    content.append(
    Paragraph(
        "<b>Key Findings</b>",
        styles["Heading2"]
    )
)

    for finding in executive_summary["key_findings"]:

        content.append(
        Paragraph(
            f"• {finding}",
            styles["BodyText"]
        )
    )

    content.append(
    Spacer(1, 25)
)

    # ==========================================================
# WEBSITE AVAILABILITY ANALYSIS
# ==========================================================

    content.append(
    Paragraph(
        "Website Availability Analysis",
        styles["Heading1"]
    )
)

    availability_data = [

    ["Field", "Value"],

    ["Meaning", cell(availability_report["meaning"], styles)],

    ["Status", availability_report["status"]],

    ["HTTP Code", str(availability_report["http_code"])],

    ["Reason", cell(availability_report["reason"], styles)],

    ["Business Impact", cell(availability_report["impact"], styles)],

    ["Recommendation", cell(availability_report["recommendation"], styles)]

]

    availability_table = Table(
    availability_data,
    colWidths=[160, 330]
)

    availability_table.setStyle(
    TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BOTTOMPADDING",(0,0),(-1,0),8)
    ])
)

    content.append(
    availability_table
)

    content.append(
    Spacer(1,20)
)

# ==========================================================
# HTTPS ANALYSIS
# ==========================================================

    content.append(
    Paragraph(
        "HTTPS Analysis",
        styles["Heading1"]
    )
)

    https_data = [

    ["Field", "Value"],

   ["Meaning", cell(https_report["meaning"], styles)],

    ["Status", https_report["status"]],

    ["Message", https_report["message"]],

   ["Reason", cell(https_report["reason"], styles)],

   ["Business Impact", cell(https_report["impact"], styles)],

   ["Recommendation", cell(https_report["recommendation"], styles)]

]

    https_table = Table(
    https_data,
    colWidths=[160,330]
)

    https_table.setStyle(
    TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BOTTOMPADDING",(0,0),(-1,0),8)
    ])
)

    content.append(
    https_table
)

    content.append(
    Spacer(1,20)
)

# ==========================================================
# SSL CERTIFICATE ANALYSIS
# ==========================================================

    content.append(
    Paragraph(
        "SSL Certificate Analysis",
        styles["Heading1"]
    )
)

    ssl_data = [

    ["Field","Value"],

    ["Meaning", cell(ssl_report["meaning"], styles)],

    ["Status", ssl_report["status"]],

    ["Certificate Issuer", ssl_report["issuer"]],

    ["Expiry Date", ssl_report["expiry_date"]],

    ["Days Remaining", str(ssl_report["days_remaining"])],

    ["Reason", cell(ssl_report["reason"], styles)],

    ["Business Impact", cell(ssl_report["impact"], styles)],

    ["Recommendation", cell(ssl_report["recommendation"], styles)]
]

    ssl_table = Table(
    ssl_data,
    colWidths=[160,330]
)

    ssl_table.setStyle(
    TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BOTTOMPADDING",(0,0),(-1,0),8)
    ])
)

    content.append(
    ssl_table
)

    content.append(
    Spacer(1,25)
)
    
    # ==========================================================
# SECURITY HEADERS ANALYSIS
# ==========================================================

    content.append(
    Paragraph(
        "Security Headers Analysis",
        styles["Heading1"]
    )
)

    content.append(
    Spacer(1,10)
)

    for finding in security_findings:

        content.append(
        Paragraph(
            finding["title"],
            styles["Heading2"]
        )
    )

    security_data = [

        ["Field", "Value"],

        ["Status", finding["status"]],

        ["Severity", finding["severity"]],

        ["Meaning", cell(finding["meaning"], styles)],

        ["Business Impact", cell(finding["impact"], styles)],

        ["Recommendation", cell(finding["recommendation"], styles)]

    ]

    security_table = Table(
        security_data,
        colWidths=[160,330]
    )

    security_table.setStyle(
        TableStyle([
            ("GRID",(0,0),(-1,-1),1,colors.black),
            ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
            ("VALIGN",(0,0),(-1,-1),"TOP"),
            ("BOTTOMPADDING",(0,0),(-1,0),8)
        ])
    )

    content.append(
        security_table
    )

    content.append(
        Spacer(1,15)
    )

    # ==========================================================
# COOKIE SECURITY ANALYSIS
# ==========================================================

    content.append(
    Paragraph(
        "Cookie Security Analysis",
        styles["Heading1"]
    )
)

    content.append(
    Spacer(1,10)
)

    for cookie in cookie_report:

        content.append(
             Paragraph(
               f"Cookie : {cookie['name']}",
               styles["Heading2"]
        )
    )

        cookie_data = [

        ["Field", "Value"],

        ["Meaning", cell(cookie["meaning"], styles)],

        ["Secure Attribute", cookie["secure"]],

        ["HttpOnly Attribute", cookie["httponly"]],

        ["SameSite Attribute", cookie["samesite"]],

        ["Business Impact", cell(cookie["impact"], styles)],

        ["Recommendation", cell(cookie["recommendation"], styles)]

    ]

        cookie_table = Table(
        cookie_data,
        colWidths=[160,330]
    )

        cookie_table.setStyle(
        TableStyle([
            ("GRID",(0,0),(-1,-1),1,colors.black),
            ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
            ("VALIGN",(0,0),(-1,-1),"TOP"),
            ("BOTTOMPADDING",(0,0),(-1,0),8)
        ])
    )

        content.append(
        cookie_table
    )

        content.append(
        Spacer(1,15)
    )

    # ==========================================================
# BROKEN LINK ANALYSIS
# ==========================================================

    content.append(
    Paragraph(
        "Broken Link Analysis",
        styles["Heading1"]
    )
)

    content.append(
    Spacer(1,10)
)

    for link in broken_link_report:

        content.append(
        Paragraph(
            link["url"],
            styles["Heading2"]
        )
    )

    broken_link_data = [

        ["Field", "Value"],

        ["Meaning", cell(link["meaning"], styles)],

        ["Status", link["status"]],

        ["HTTP Status Code", str(link["http_code"])],

        ["Business Impact", cell(link["impact"], styles)],

        ["Recommendation", cell(link["recommendation"], styles)]

    ]

    broken_link_table = Table(
        broken_link_data,
        colWidths=[160,330]
    )

    broken_link_table.setStyle(
        TableStyle([
            ("GRID",(0,0),(-1,-1),1,colors.black),
            ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
            ("VALIGN",(0,0),(-1,-1),"TOP"),
            ("BOTTOMPADDING",(0,0),(-1,0),8)
        ])
    )

    content.append(
        broken_link_table
    )

    content.append(
        Spacer(1,15)
    )

    # ==========================================================
# ROBOTS.TXT ANALYSIS
# ==========================================================

    content.append(
    Paragraph(
        "Robots.txt Analysis",
        styles["Heading1"]
    )
)

    content.append(
    Spacer(1,10)
)

    robots_data = [

    ["Field", "Value"],

    ["Meaning", cell(robots_report["meaning"], styles)],

    ["Status", robots_report["status"]],

    ["Reason", cell(robots_report["reason"], styles)],

    ["Business Impact", cell(robots_report["impact"], styles)],

    ["Recommendation", cell(robots_report["recommendation"], styles)]

]

    robots_table = Table(
    robots_data,
    colWidths=[160,330]
)

    robots_table.setStyle(
    TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BOTTOMPADDING",(0,0),(-1,0),8)
    ])
)

    content.append(
    robots_table
)

    content.append(
    Spacer(1,20)
)

# ==========================================================
# SITEMAP ANALYSIS
# ==========================================================

    content.append(
    Paragraph(
        "Sitemap Analysis",
        styles["Heading1"]
    )
)

    content.append(
    Spacer(1,10)
)

    sitemap_data = [

    ["Field","Value"],

    ["Meaning", cell(sitemap_report["meaning"], styles)],

    ["Status", sitemap_report["status"]],

    ["URLs Found", str(sitemap_report["url_count"])],

    ["Reason", cell(sitemap_report["reason"], styles)],

    ["Business Impact", cell(sitemap_report["impact"], styles)],

    ["Recommendation", cell(sitemap_report["recommendation"], styles)]

]

    sitemap_table = Table(
    sitemap_data,
    colWidths=[160,330]
)

    sitemap_table.setStyle(
    TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BOTTOMPADDING",(0,0),(-1,0),8)
    ])
)

    content.append(
    sitemap_table
)

    content.append(
    Spacer(1,20)
)

# ==========================================================
# MOBILE FRIENDLY ANALYSIS
# ==========================================================

    content.append(
    Paragraph(
        "Mobile Friendly Analysis",
        styles["Heading1"]
    )
)

    content.append(
    Spacer(1,10)
)

    mobile_data = [

    ["Field","Value"],

    ["Meaning", cell(mobile_report["meaning"], styles)],

    ["Status", mobile_report["status"]],

    ["Reason", cell(mobile_report["reason"], styles)],

    ["Business Impact", cell(mobile_report["impact"], styles)],

    ["Recommendation", cell(mobile_report["recommendation"], styles)]

]

    mobile_table = Table(
    mobile_data,
    colWidths=[160,330]
)

    mobile_table.setStyle(
    TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BOTTOMPADDING",(0,0),(-1,0),8)
    ])
)

    content.append(
    mobile_table
)

    content.append(
    Spacer(1,25)
)

# ==========================================================
# SENSITIVE FILES ANALYSIS
# ==========================================================

    content.append(
    Paragraph(
        "Sensitive Files Analysis",
        styles["Heading1"]
    )
)

    content.append(
    Spacer(1,10)
)

    sensitive_data = [

    ["Field","Value"],

    ["Meaning", cell(sensitive_files_report["meaning"], styles)],

    ["Status", sensitive_files_report["status"]],

    ["Files Exposed", str(sensitive_files_report["files_found"])],

    ["Reason", cell(sensitive_files_report["reason"], styles)],

    ["Business Impact", cell(sensitive_files_report["impact"], styles)],

    ["Recommendation", cell(sensitive_files_report["recommendation"], styles)]

]

    sensitive_table = Table(
    sensitive_data,
    colWidths=[160,330]
)

    sensitive_table.setStyle(
    TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BOTTOMPADDING",(0,0),(-1,0),8)
    ])
)

    content.append(
    sensitive_table
)

    if sensitive_files_report["files_found"] > 0:

        content.append(
        Spacer(1,10)
    )

    content.append(
        Paragraph(
            "<b>Exposed Files</b>",
            styles["Heading2"]
        )
    )

    for file in sensitive_files_report["exposed_files"]:

        content.append(
            Paragraph(
                f"• {file}",
                styles["BodyText"]
            )
        )

    content.append(
    Spacer(1,25)
)

# ==========================================================
# TECHNOLOGY DETECTION ANALYSIS
# ==========================================================

    content.append(
    Paragraph(
        "Technology Detection Analysis",
        styles["Heading1"]
    )
)

    content.append(
    Spacer(1,10)
)

    technology_data = [

    ["Field","Value"],

    [
    "Meaning",
    Paragraph(
        technology_report["meaning"],
        styles["BodyText"]
    )
],

    ["Status", technology_report["status"]],

    ["Server", technology_report["server"]],

    ["Framework", technology_report["framework"]],

    ["Programming Language", technology_report["language"]],

    ["Technologies Detected", str(technology_report["technology_count"])],

    ["Reason", cell(technology_report["reason"], styles)],

    ["Business Impact", cell(technology_report["impact"], styles)],

    ["Recommendation", cell(technology_report["recommendation"], styles)]

]

    technology_table = Table(
    technology_data,
    colWidths=[160,330]
)

    technology_table.setStyle(
    TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BOTTOMPADDING",(0,0),(-1,0),8)
    ])
)

    content.append(
    technology_table
)

    if technology_report["technology_count"] > 0:

        content.append(
        Spacer(1,10)
    )

    content.append(
        Paragraph(
            "Detected Technologies",
            styles["Heading2"]
        )
    )

    for tech in technology_report["technologies"]:

        content.append(
            Paragraph(
                f"• {tech}",
                styles["BodyText"]
            )
        )

    content.append(
    Spacer(1,25)
)

# ==========================================================
# DIRECTORY LISTING ANALYSIS
# ==========================================================

    content.append(
    Paragraph(
        "Directory Listing Analysis",
        styles["Heading1"]
    )
)

    content.append(
    Spacer(1,10)
)

    directory_data = [

    ["Field","Value"],

    ["Meaning", cell(directory_listing_report["meaning"], styles)],

    ["Status", directory_listing_report["status"]],

    ["Reason", cell(directory_listing_report["reason"], styles)],

    ["Business Impact", cell(directory_listing_report["impact"], styles)],

    ["Recommendation", cell(directory_listing_report["recommendation"], styles)]

]

    directory_table = Table(
    directory_data,
    colWidths=[160,330]
)

    directory_table.setStyle(
    TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BOTTOMPADDING",(0,0),(-1,0),8)
    ])
)

    content.append(
    directory_table
)
    content.append(
    Spacer(1,10)
)

    content.append(
    Paragraph(
        "Directories Checked",
        styles["Heading2"]
    )
)

    for directory in directory_listing_report["directories"]:

        content.append(
        Paragraph(
            f"• {directory['path']} : {directory['status']}",
            styles["BodyText"]
        )
    )

    content.append(
    Spacer(1,25)
)

# ==========================================================
# PERFORMANCE ANALYSIS
# ==========================================================

    content.append(
    Paragraph(
        "Performance Analysis",
        styles["Heading1"]
    )
)

    content.append(
    Spacer(1,10)
)

    performance_data = [

    ["Field","Value"],

    ["Meaning", cell(performance_report["meaning"], styles)],

    ["Status", performance_report["status"]],

    ["Performance Score", str(performance_report["score"]) + "/100"],

    ["Load Time", str(performance_report["load_time"]) + " Seconds"],

    ["Page Size", str(performance_report["page_size"]) + " KB"],

    ["Images Detected", str(performance_report["images"])],

    ["JavaScript Files", str(performance_report["scripts"])],

    ["Reason", cell(performance_report["reason"], styles)],

    ["Business Impact", cell(performance_report["impact"], styles)],

    ["Recommendation", cell(performance_report["recommendation"], styles)]

]

    performance_table = Table(
    performance_data,
    colWidths=[160,330]
)

    performance_table.setStyle(
    TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BOTTOMPADDING",(0,0),(-1,0),8)
    ])
)

    content.append(
    performance_table
)

    content.append(
    Spacer(1,25)
)

# ==========================================================
# ACCESSIBILITY ANALYSIS
# ==========================================================

    content.append(
    Paragraph(
        "Accessibility Analysis",
        styles["Heading1"]
    )
)

    content.append(
    Spacer(1,10)
)

    accessibility_data = [

    ["Field","Value"],

    ["Meaning", cell(accessibility_report["meaning"], styles)],

    ["Status", accessibility_report["status"]],

    ["Accessibility Score", str(accessibility_report["score"]) + "%"],

    ["Checks Passed", str(accessibility_report["passed"])],

    ["Total Checks", str(accessibility_report["total"])],

    ["Reason", cell(accessibility_report["reason"], styles)],

    ["Business Impact", cell(accessibility_report["impact"], styles)],

    ["Recommendation", cell(accessibility_report["recommendation"], styles)]

]

    accessibility_table = Table(
    accessibility_data,
    colWidths=[160,330]
)

    accessibility_table.setStyle(
    TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BOTTOMPADDING",(0,0),(-1,0),8)
    ])
)

    content.append(
    accessibility_table
)

    content.append(
    Spacer(1,25)
)

# ==========================================================
# DOMAIN INFORMATION ANALYSIS
# ==========================================================

    content.append(
    Paragraph(
        "Domain Information Analysis",
        styles["Heading1"]
    )
)

    content.append(
    Spacer(1,10)
)

    domain_data = [

    ["Field","Value"],

    ["Meaning", cell(domain_info_report["meaning"], styles)],

    ["Status", domain_info_report["status"]],

    ["Domain", domain_info_report["domain"]],

    ["Registrar", domain_info_report["registrar"]],

    ["Created", domain_info_report["created"]],

    ["Expires", domain_info_report["expires"]],

    ["Days Remaining", str(domain_info_report["days_remaining"])],

    ["Reason", cell(domain_info_report["reason"], styles)],

    ["Business Impact", cell(domain_info_report["impact"], styles)],

    ["Recommendation", cell(domain_info_report["recommendation"], styles)]

]

    domain_table = Table(
    domain_data,
    colWidths=[160,330]
)

    domain_table.setStyle(
    TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BOTTOMPADDING",(0,0),(-1,0),8)
    ])
)

    content.append(
    domain_table
)

    content.append(
    Spacer(1,25)
)

# ==========================================================
# EMAIL SECURITY ANALYSIS
# ==========================================================

    content.append(
    Paragraph(
        "Email Security Analysis",
        styles["Heading1"]
    )
)

    content.append(
    Spacer(1,10)
)

    email_data = [

    ["Field","Value"],

    ["Meaning", cell(email_security_report["meaning"], styles)],

    ["Status", email_security_report["status"]],

    ["Security Score", str(email_security_report["score"]) + "%"],

    ["Checks Passed", str(email_security_report["passed"])],

    ["Total Checks", str(email_security_report["total"])],

    ["Reason", cell(email_security_report["reason"], styles)],

    ["Business Impact", cell(email_security_report["impact"], styles)],

    ["Recommendation", cell(email_security_report["recommendation"], styles)]

]

    email_table = Table(
    email_data,
    colWidths=[160,330]
)

    email_table.setStyle(
    TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BOTTOMPADDING",(0,0),(-1,0),8)
    ])
)

    content.append(
    email_table
)

    content.append(
    Spacer(1,25)
)

# ==========================================================
# OPEN PORTS ANALYSIS
# ==========================================================

    content.append(
    Paragraph(
        "Open Ports Analysis",
        styles["Heading1"]
    )
)

    content.append(
    Spacer(1,10)
)

    ports_data = [

    ["Field","Value"],

    ["Meaning", cell(ports_report["meaning"], styles)],

    ["Status", ports_report["status"]],

    ["Open Ports", str(ports_report["open_ports"])],

    ["Ports Scanned", str(ports_report["total"])],

    ["Reason", cell(ports_report["reason"], styles)],

    ["Business Impact", cell(ports_report["impact"], styles)],

    ["Recommendation", cell(ports_report["recommendation"], styles)]

]

    ports_table = Table(
    ports_data,
    colWidths=[160,330]
)

    ports_table.setStyle(
    TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BOTTOMPADDING",(0,0),(-1,0),8)
    ])
)

    content.append(
    ports_table
)

    content.append(
    Spacer(1,25)
)

# ==========================================================
# FINAL CONCLUSION
# ==========================================================

    content.append(
    Paragraph(
        "Final Conclusion",
        styles["Heading1"]
    )
)

    content.append(
    Spacer(1,10)
)

    conclusion_data = [

    ["Field","Value"],

    ["Website", final_conclusion["website"]],

    ["Overall Score", str(final_conclusion["overall_score"]) + "/100"],

    ["Overall Rating", final_conclusion["verdict"]],

    ["Critical Issues", str(final_conclusion["critical"])],

    ["Medium Issues", str(final_conclusion["medium"])],

    ["Low Issues", str(final_conclusion["low"])]

]

    conclusion_table = Table(
    conclusion_data,
    colWidths=[160,330]
)

    conclusion_table.setStyle(
    TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BOTTOMPADDING",(0,0),(-1,0),8)
    ])
)

    content.append(
    conclusion_table
)

    content.append(
    Spacer(1,15)
)

    content.append(
    Paragraph(
        "<b>Summary</b>",
        styles["Heading2"]
    )
)

    content.append(
    Paragraph(
        final_conclusion["summary"],
        styles["BodyText"]
    )
)

    content.append(
    Spacer(1,10)
)

    content.append(
    Paragraph(
        "<b>Recommendation</b>",
        styles["Heading2"]
    )
)

    content.append(
    Paragraph(
        final_conclusion["recommendation"],
        styles["BodyText"]
    )
)

    content.append(
    Spacer(1,20)
)

    doc.build(content)

    return pdf_path