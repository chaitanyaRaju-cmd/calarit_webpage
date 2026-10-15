from django.http import HttpResponse

from django.core.mail import send_mail

from django.conf import settings

import random

from .models import OTPVerification

from django.shortcuts import render , redirect

from django.http import JsonResponse

from django.contrib.auth.models import User

from django.contrib.auth import authenticate

from django.contrib.auth import login

from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

from .screenshot_engine import capture_screenshot

from .score_engine import calculate_health_score

from .seo_engine import check_seo

from .cookie_engine import analyze_cookies

from .robots_engine import analyze_robots

from .sitemap_engine import analyze_sitemap

from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

from django.views.decorators.http import require_POST

from .scoring_engine import (
    calculate_section_scores
)

from .ports_engine import (
    analyze_ports
)

from .sensitive_files_engine import (
    analyze_sensitive_files
)

from .ssl_engine import (
    check_ssl_certificate
)

from .recommendation_engine import (
    generate_recommendations
)

from .security_engine import (
    check_security_headers
)

from .test_engine import (
    check_availability,
    check_https
)

from .issues_engine import (
    calculate_issues
)

from .pdf_engine import (
    generate_pdf_report
)

from django.http import FileResponse
import os

from .mobile_engine import (
    analyze_mobile_friendly
)

from .technology_engine import (
    detect_technologies
)

from .directory_listing_engine import (
    check_directory_listing
)

from .performance_engine import (
    analyze_performance
)

from .accessibility_engine import (
    analyze_accessibility
)

from .domain_info_engine import (
    analyze_domain_info
)

from .email_security_engine import (
    analyze_email_security
)

from .broken_link_engine import (
    check_broken_links
)

from .mobile_application_engine import (
    analyze_mobile_application
)


from .report_engine import (
    build_executive_summary,
    build_security_findings,
    build_availability_report,
    build_https_report,
    build_ssl_report,
    build_cookie_report,
    build_broken_link_report,
    build_robots_report,
    build_sitemap_report,
    build_mobile_report,
    build_sensitive_files_report,
    build_technology_report,
    build_directory_listing_report,
    build_performance_report,
    build_accessibility_report,
    build_domain_info_report,
    build_email_security_report,
    build_ports_report,
    build_final_conclusion
    
)

def home(request):

    return render(
        request,
        "index.html"
    )

def test_email(request):

    try:

        send_mail(

            subject="CALARIT SMTP Test",

            message="""
Congratulations!

Your Django SMTP configuration is working successfully.

CALARIT Backend is now connected to Gmail.

Next Step:
Real OTP Generation.

Regards,
CALARIT Team
""",

            from_email=settings.EMAIL_HOST_USER,

            recipient_list=[settings.EMAIL_HOST_USER],

            fail_silently=False,

        )

        return HttpResponse(

            "✅ Test Email Sent Successfully."

        )

    except Exception as e:

        return HttpResponse(

            f"❌ Error:<br><br>{e}"

        )
    
def generate_otp(request):

    try:

        username = request.GET.get("username")
        email = request.GET.get("email")
        password = request.GET.get("password")

        print("USERNAME =", username)
        print("EMAIL =", email)
        print("PASSWORD =", password)

        if not username or not email or not password:

           return HttpResponse(
    "❌ Username, Email and Password are required."
)

        if User.objects.filter(
             email=email
).exists():

           return HttpResponse(
        "❌ Email already registered."
    )
        
        if User.objects.filter(
            username=username
).exists():

           return HttpResponse(
        "❌ Username already exists."
    )
        otp = str(
            random.randint(
                100000,
                999999
            )
        )

        OTPVerification.objects.create(
            username=username,
            email=email,
            password=password,
            otp=otp,
            is_verified=False
        )

        send_mail(
            subject="CALARIT OTP Verification",

            message=f"""
Hello,

Your OTP is:

{otp}

This OTP is valid for verification.

Regards,
CALARIT Team
""",

            from_email=settings.EMAIL_HOST_USER,

            recipient_list=[email],

            fail_silently=False,
        )

        return HttpResponse(
            f"✅ OTP Sent Successfully.<br><br>OTP: {otp}"
        )

    except Exception as e:

        return HttpResponse(
            f"❌ Error:<br><br>{e}"
        )
    
def verify_otp(request):

    try:

        otp = request.GET.get("otp")

        if not otp:

            return JsonResponse({

                "success": False,

                "message": "OTP is required."

            })

        otp_record = OTPVerification.objects.filter(

            otp=otp,

            is_verified=False

        ).last()

        if not otp_record:

            return JsonResponse({

                "success": False,

                "message": "Invalid OTP."

            })

        # Signup Flow Only

        if otp_record.username and otp_record.password:

            if User.objects.filter(

                username=otp_record.username

            ).exists():

                return JsonResponse({

                    "success": False,

                    "message": "Username already exists."

                })

            if User.objects.filter(

                email=otp_record.email

            ).exists():

                return JsonResponse({

                    "success": False,

                    "message": "Email already registered."

                })

            User.objects.create_user(

                username=otp_record.username,

                email=otp_record.email,

                password=otp_record.password

            )

        otp_record.is_verified = True

        otp_record.save()

        return JsonResponse({

            "success": True,

            "message": "OTP verified successfully."

        })

    except Exception as e:

        return JsonResponse({

            "success": False,

            "message": str(e)

        })
    
def login_user(request):

    try:

        username = request.GET.get("username")
        password = request.GET.get("password")

        if not username or not password:

            return JsonResponse({

                "success": False,

                "message": "Username and Password required."

            })

        user = authenticate(

            request,

            username=username,

            password=password

        )

        if user is None:

            return JsonResponse({

                "success": False,

                "message": "Invalid credentials."

            })

        login(request, user)

        return JsonResponse({

    "success": True,

    "redirect": "/dashboard/"

})

    except Exception as e:

        return JsonResponse({

            "success": False,

            "message": str(e)

        })
    
def forgot_password_otp(request):

    try:

        email = request.GET.get("email")

        if not email:

            return JsonResponse({

                "success": False,

                "message": "Email is required."

            })

        from django.contrib.auth.models import User

        if not User.objects.filter(
            email=email
        ).exists():

            return JsonResponse({

                "success": False,

                "message": "Email not registered."

            })

        otp = str(
            random.randint(
                100000,
                999999
            )
        )

        OTPVerification.objects.create(

            email=email,

            otp=otp,

            is_verified=False

        )

        send_mail(

            subject="CALARIT Password Reset OTP",

            message=f"""
Hello,

Your Password Reset OTP is:

{otp}

Regards,
CALARIT Team
""",

            from_email=settings.EMAIL_HOST_USER,

            recipient_list=[email],

            fail_silently=False

        )

        return JsonResponse({

            "success": True,

            "message": "OTP sent successfully."

        })

    except Exception as e:

        return JsonResponse({

            "success": False,

            "message": str(e)

        })
    
def reset_password(request):

    try:

        email = request.GET.get("email")

        password = request.GET.get("password")

        if not email or not password:

            return JsonResponse({

                "success": False,

                "message": "Email and Password are required."

            })

        user = User.objects.filter(

            email=email

        ).first()

        if not user:

            return JsonResponse({

                "success": False,

                "message": "User not found."

            })

        user.set_password(

            password

        )

        user.save()

        return JsonResponse({

            "success": True,

            "message": "Password updated successfully."

        })

    except Exception as e:

        return JsonResponse({

            "success": False,

            "message": str(e)

        })
    
def dashboard(request):

    if not request.user.is_authenticated:

        return redirect("/")

    return render(

        request,

        "dashboard.html"

    )

def logout_user(request):

    logout(request)

    return redirect("/")

@login_required(login_url='/')
def website_testing(request):

    if request.method == "POST":

        website_url = request.POST.get(
            "website_url"
        )

        request.session[
            "website_url"
        ] = website_url

        return redirect(
            "testing_progress"
        )

    return render(
        request,
        "website_testing.html"
    )

@login_required(login_url='/')
def mobile_testing(request):

    return render(
        request,
        "mobile_testing.html"
    )

@login_required(login_url='/')
def testing_progress(request):

    return render(
        request,
        "testing_progress.html"
    )

@login_required(login_url='/')
def results_dashboard(request):

    website_url = request.session.get(
        "website_url",
        ""
    )

    availability_result = (
        check_availability(
            website_url
        )
    )

    screenshot = capture_screenshot(
    website_url
)
    request.session["screenshot"] = screenshot.replace(
    "/media/",
    "media/"
)
    
    

    https_result = (
        check_https(
            website_url
        )
    )

    health_result = (
    calculate_health_score(
        availability_result,
        https_result
    )
)
    
    security_results = (
    check_security_headers(
        website_url
    )
)
    
    seo_results = check_seo(
    website_url
)
    
    mobile_result = (
    analyze_mobile_friendly(
        website_url
    )
)
    
    sensitive_files_result = (
    analyze_sensitive_files(
        website_url
    )
)
    
    ssl_result = (
    check_ssl_certificate(
        website_url
    )
)
    
    broken_links = (
    check_broken_links(
        website_url
    )[:20]
)
    
    cookie_results = analyze_cookies(
    website_url
)
    
    robots_result = analyze_robots(
    website_url
)
    

    
    broken_link_failures = len([
    x
    for x in broken_links
    if x["status"] == "FAIL"
   ]

)
    
    sitemap_result = (
    analyze_sitemap(
        website_url
    )
)
    
    sensitive_files_result = (
    analyze_sensitive_files(
        website_url
    )
)

    technology_results = (
    detect_technologies(
        website_url
    )
)
    
    
    directory_listing_result = (
    check_directory_listing(
        website_url
    )
)
    
    performance_result = (
    analyze_performance(
        website_url
    )
)
    
    accessibility_results = (
    analyze_accessibility(
        website_url
    )
)
    
    passed = len([
    x for x in accessibility_results
    if x["status"] == "PASS"
])
    
    total = len(accessibility_results)
    score = round((passed / total) * 100) if total else 0
    if score >= 80:
     overall_status = "PASS"
    elif score >= 60:
     overall_status = "WARNING"
    else:
     overall_status = "FAIL"

    accessibility_summary = {

    "score": score,

    "status": overall_status,

    "summary":
    f"{passed} of {total} accessibility checks passed."

}
    
    domain_info_result = (
    analyze_domain_info(
        website_url
    )
)
    
    email_security_results = (
    analyze_email_security(
        website_url
    )
)
    
    ports_results = (
    analyze_ports(
        website_url
    )
)
    
    section_scores = (
    calculate_section_scores(
        security_results,
        seo_results,
        accessibility_results,
        performance_result
    )
)
    
    recommendations = (
    generate_recommendations(
        security_results,
        seo_results,
        sitemap_result,
        mobile_result,
        sensitive_files_result,
        technology_results,
        directory_listing_result,
        performance_result,
        accessibility_results,
        domain_info_result,
        email_security_results,
        ports_results,
        section_scores
    )
)
    
    issues_summary = (
    calculate_issues(
        security_results,
        seo_results,
        robots_result,
        sensitive_files_result,
        directory_listing_result,
        accessibility_results,
        domain_info_result,
        email_security_results,
        ports_results,
        
    )
)
    
    print(cookie_results)
    print(len(cookie_results))
    


    context = {

     "website_url": website_url,

        "availability_result":
        availability_result,

        "https_result":
        https_result,

        "screenshot":
        screenshot,

        "health_result":
        health_result,

        "security_results":
        security_results,

        "seo_results":
        seo_results,

        "ssl_result":
        ssl_result,

        "broken_links":
        broken_links,

        "cookie_results": 
        cookie_results,

        "robots_result": 
        robots_result,

        "sitemap_result":
        sitemap_result,

        "mobile_result":
        mobile_result,

        "sensitive_files_result":
        sensitive_files_result,

        "technology_results":
        technology_results,

        "directory_listing_result":
        directory_listing_result,

        "performance_result":
        performance_result,

        "accessibility_results":
        accessibility_results,

        "domain_info_result":
        domain_info_result,

        "email_security_results":
        email_security_results,

        "ports_results":
        ports_results,

        "section_scores":
        section_scores,

        "broken_link_failures":
        broken_link_failures,

        "recommendations":
        recommendations,

        "issues_summary":
        issues_summary,

    

    
}
    context["accessibility_summary"] = accessibility_summary
    
    # ==========================================
# Build Professional Report Data
# ==========================================

    executive_summary = build_executive_summary(
    website_url,
    section_scores,
    https_result,
    ssl_result,
    issues_summary
)

    security_findings = build_security_findings(
    security_results
)
    
    availability_report = build_availability_report(
    availability_result
)
    
    https_report = build_https_report(
    https_result
)
    
    ssl_report = build_ssl_report(
    ssl_result
)
    
    cookie_report = build_cookie_report(
    cookie_results
)
    
    broken_link_report = build_broken_link_report(
    broken_links
)
    
    robots_report = build_robots_report(
    robots_result
)
    
    sitemap_report = build_sitemap_report(
    sitemap_result
)
    
    mobile_report = build_mobile_report(
    mobile_result
)
    
    sensitive_files_report = build_sensitive_files_report(
    sensitive_files_result
)
    
    technology_report = build_technology_report(
    technology_results
)
    
    directory_listing_report = build_directory_listing_report(
    directory_listing_result
)
    
    accessibility_report = build_accessibility_report(
    accessibility_results
)
    
    domain_info_report = build_domain_info_report(
    domain_info_result
)
    
    email_security_report = build_email_security_report(
    email_security_results
)
    
    ports_report = build_ports_report(
    ports_results
)
    
    final_conclusion = build_final_conclusion(
    website_url,
    section_scores,
    issues_summary
)
    
    performance_report = build_performance_report(
    performance_result
)
    
    
    

    context["executive_summary"] = executive_summary
    context["security_findings"] = security_findings
    context["availability_report"] = availability_report
    context["https_report"] = https_report
    context["ssl_report"] = ssl_report
    context["cookie_report"] = cookie_report
    context["broken_link_report"] = broken_link_report
    context["robots_report"] = robots_report
    context["sitemap_report"] = sitemap_report
    context["mobile_report"] = mobile_report
    context["sensitive_files_report"] = sensitive_files_report
    context["technology_report"] = technology_report
    context["directory_listing_report"] = directory_listing_report
    context["directory_listing_result"] = directory_listing_result
    context["performance_report"] = performance_report
    context["accessibility_report"] = accessibility_report
    context["accessibility_results"] = accessibility_results
    context["domain_info_report"] = domain_info_report
    context["email_security_report"] = email_security_report
    context["ports_report"] = ports_report
    context["final_conclusion"] = final_conclusion

    return render(
    request,
    "results_dashboard.html",
    context
)


@login_required(login_url='/')
def download_pdf(request):

    website_url = request.session.get(
        "website_url",
        ""
    )

    availability_result = (
        check_availability(
            website_url
        )
    )

    https_result = (
        check_https(
            website_url
        )
    )

    health_result = (
        calculate_health_score(
            availability_result,
            https_result
        )
    )

    security_results = (
        check_security_headers(
            website_url
        )
    )

    seo_results = (
        check_seo(
            website_url
        )
    )

    sitemap_result = (
    analyze_sitemap(
        website_url
    )
)
    
    mobile_result = (
    analyze_mobile_friendly(
        website_url
    )
)
    
    sensitive_files_result = (
    analyze_sensitive_files(
        website_url
    )
)
    
    technology_results = (
    detect_technologies(
        website_url
    )
)
    directory_listing_result = (
    check_directory_listing(
        website_url
    )
)
    
    performance_result = (
    analyze_performance(
        website_url
    )
)
    accessibility_results = (
    analyze_accessibility(
        website_url
    )
)
    
    
    domain_info_result = (
    analyze_domain_info(
        website_url
    )
)
    
    email_security_results = (
    analyze_email_security(
        website_url
    )
)
    
    ports_results = (
    analyze_ports(
        website_url
    )
)
    
    ssl_result = (
    check_ssl_certificate(
        website_url
    )
)
    
    broken_links = (
    check_broken_links(
        website_url
    )[:20]
)
    
    cookie_results = analyze_cookies(
    website_url
)
    
    robots_result = analyze_robots(
    website_url
)
    
    section_scores = (
    calculate_section_scores(
        security_results,
        seo_results,
        accessibility_results,
        performance_result
    )
)

    recommendations = (
    generate_recommendations(
        security_results,
        seo_results,
        sitemap_result,
        mobile_result,
        sensitive_files_result,
        technology_results,
        directory_listing_result,
        performance_result,
        accessibility_results,
        domain_info_result,
        email_security_results,
        ports_results,
        section_scores
    )
)
    pdf_path = os.path.join(
        "media",
        "reports",
        "calarit_report.pdf"
    )

    os.makedirs(
        os.path.dirname(pdf_path),
        exist_ok=True
    )

    screenshot_path = request.session.get(
    "screenshot",
    None
)
    
    section_scores = calculate_section_scores(
    security_results,
    seo_results,
    accessibility_results,
    performance_result
)
    
    issues_summary = calculate_issues(
    security_results,
    seo_results,
    robots_result,
    sensitive_files_result,
    directory_listing_result,
    accessibility_results,
    domain_info_result,
    email_security_results,
    ports_results
)

    executive_summary = build_executive_summary(
    website_url,
    section_scores,
    https_result,
    ssl_result,
    issues_summary
)

    security_findings = build_security_findings(
    security_results
)
    
    availability_report = build_availability_report(
    availability_result
)
    
    https_report = build_https_report(
    https_result
)
    
    ssl_report = build_ssl_report(
    ssl_result
)
    
    cookie_report = build_cookie_report(
    cookie_results
)
    
    broken_link_report = build_broken_link_report(
    broken_links
)
    
    robots_report = build_robots_report(
    robots_result
)
    
    sitemap_report = build_sitemap_report(
    sitemap_result
)
    
    mobile_report = build_mobile_report(
    mobile_result
)
    
    sensitive_files_report = build_sensitive_files_report(
    sensitive_files_result
)
    
    technology_report = build_technology_report(
    technology_results
)
    
    directory_listing_report = build_directory_listing_report(
    directory_listing_result
)
    
    accessibility_report = build_accessibility_report(
    accessibility_results
)
    
    domain_info_report = build_domain_info_report(
    domain_info_result
)
    
    email_security_report = build_email_security_report(
    email_security_results
)
    
    ports_report = build_ports_report(
    ports_results
)
    
    final_conclusion = build_final_conclusion(
    website_url,
    section_scores,
    issues_summary
)
    
    performance_report = build_performance_report(
    performance_result
)

    generate_pdf_report(
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
)

    return FileResponse(
        open(pdf_path, "rb"),
        as_attachment=True,
        filename="CALARIT_Report.pdf"
    )

from django.http import JsonResponse

@require_POST
@login_required(login_url="/")
def upload_mobile_apk_view(request):

    print("========== UPLOAD API CALLED ==========")

    uploaded_apk = request.FILES.get("apk")

    if uploaded_apk is None:

        return JsonResponse({

            "success": False,

            "message": "No APK uploaded."

        })

    upload_directory = os.path.join(
        settings.MEDIA_ROOT,
        "mobile_uploads"
    )

    os.makedirs(
        upload_directory,
        exist_ok=True
    )

    storage = FileSystemStorage(
        location=upload_directory
    )

    saved_file_name = storage.save(
        uploaded_apk.name,
        uploaded_apk
    )

    apk_path = storage.path(
        saved_file_name
    )

    analysis_result = analyze_mobile_application(
    apk_path
)

    return JsonResponse({

    "success": True,

    "upload": {

        "apk_name": saved_file_name,

        "apk_path": apk_path

    },

    "application_engine": analysis_result

})