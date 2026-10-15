def generate_recommendations(
    security_results,
    seo_results,
    sitemap_result,
    mobile_result,
    sensitive_files_result,
    technology_results,
    directory_results,
    performance_result,
    accessibility_results,
    domain_info_result,
    email_security_results,
    ports_results,
    section_scores
):
    recommendations = []

    for item in security_results:

        if item["status"] == "FAIL":

            recommendations.append(
                f"Fix security issue: {item['name']}"
            )

    for item in seo_results:

        if item["status"] == "FAIL":

            recommendations.append(
                f"Improve SEO: {item['name']}"
            )

    for tech in technology_results:

        recommendations.append(
        f"Technology detected: {tech}"
    )
        
    if section_scores["overall_score"] < 80:

        recommendations.append(
        "Overall website score can be improved."
    )

    if sitemap_result["status"] == "FAIL":

        recommendations.append(
            "Create sitemap.xml for better SEO indexing."
        )

    if mobile_result["status"] == "FAIL":

        recommendations.append(
            "Add mobile viewport meta tag for mobile friendliness."
        )

        for item in sensitive_files_result:

          if item["status"] == "FAIL":

             recommendations.append(
            f"Sensitive file exposed: {item['file']}"
        )
             
        for item in directory_results:

          if item["status"] == "FAIL":

            recommendations.append(
            f"Directory listing enabled: {item['path']}"
        )
            
          if performance_result["score"] < 80:

             recommendations.append(
             "Improve website performance and loading speed."
    )

        for item in accessibility_results:

           if item["status"] == "FAIL":

             recommendations.append(

            f"Improve accessibility: {item['name']}"

        )
             
    if domain_info_result["days_remaining"] < 90:

      recommendations.append(
        "Domain expires soon. Consider renewing it."
    )
         
    for item in email_security_results:

           if item["status"] == "FAIL":

             recommendations.append(

            f"Configure {item['name']} for email security."

        )
             
           for item in ports_results:

              if item["status"] == "OPEN":

                if item["port"] not in [80, 443]:

                   recommendations.append(
                   f"Review open port {item['port']} ({item['service']})."
            )


    if not recommendations:

        recommendations.append(
            "No major issues detected."
        )

    return recommendations