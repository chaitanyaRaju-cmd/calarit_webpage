def calculate_section_scores(

    security_results,
    seo_results,
    accessibility_results,
    performance_result

):

    security_pass = len([
        x for x in security_results
        if x["status"] == "PASS"
    ])

    seo_pass = len([
        x for x in seo_results
        if x["status"] == "PASS"
    ])

    accessibility_pass = len([
        x for x in accessibility_results
        if x["status"] == "PASS"
    ])

    security_score = int(
        (security_pass / len(security_results)) * 100
    )

    seo_score = int(
        (seo_pass / len(seo_results)) * 100
    )

    accessibility_score = int(
        (
            accessibility_pass
            /
            len(accessibility_results)
        ) * 100
    )

    performance_score = (
        performance_result["score"]
    )

    overall_score = int(

        (
            security_score
            +
            seo_score
            +
            accessibility_score
            +
            performance_score
        ) / 4

    )

    if overall_score >= 90:
       risk_level = "Low"

    elif overall_score >= 75:
      risk_level = "Medium"

    elif overall_score >= 50:
      risk_level = "High"

    else:
      risk_level = "Critical"

    def get_status(score):

        if score >= 90:
            return "EXCELLENT"

        elif score >= 75:
            return "GOOD"

        elif score >= 50:
            return "WARNING"

        else:
            return "CRITICAL"

    return {

    "security_score": security_score,
    "security_status": get_status(security_score),

    "seo_score": seo_score,
    "seo_status": get_status(seo_score),

    "accessibility_score": accessibility_score,
    "accessibility_status": get_status(accessibility_score),

    "performance_score": performance_score,
    "performance_status": get_status(performance_score),

    "overall_score": overall_score,

    "risk_level": risk_level

}