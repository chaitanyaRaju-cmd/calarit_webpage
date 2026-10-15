def calculate_health_score(
    availability_result,
    https_result
):

    score = 0

    # Availability
    if availability_result["status"] == "PASS":
        score += 50

    # HTTPS
    if https_result["status"] == "PASS":
        score += 30

    # Security (placeholder)
    score += 10

    # SEO (placeholder)
    score += 10

    if score >= 90:
        rating = "EXCELLENT"

    elif score >= 75:
        rating = "GOOD"

    elif score >= 60:
        rating = "FAIR"

    else:
        rating = "POOR"

    return {
        "score": score,
        "rating": rating
    }