from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home",
    ),

    path(
        "test-email/",
        views.test_email,
        name="test_email",
    ),

    path(
        "generate-otp/",
        views.generate_otp,
        name="generate_otp",
    ),

    path(
        "verify-otp/",
        views.verify_otp,
        name="verify_otp",
    ),

    path(
    "login-user/",
    views.login_user,
    name="login_user"
),

   path(
    "forgot-password-otp/",
    views.forgot_password_otp,
    name="forgot_password_otp"
),

path(
    "reset-password/",
    views.reset_password,
    name="reset_password"
),

path(
    "dashboard/",
    views.dashboard,
    name="dashboard"
),

path(
    "logout/",
    views.logout_user,
    name="logout_user"
),

path(
    "website-testing/",
    views.website_testing,
    name="website_testing"
),

path(
    "mobile-testing/",
    views.mobile_testing,
    name="mobile_testing"
),

path(
    "mobile-testing/application-analysis/",
    views.upload_mobile_apk_view,
    name="mobile_application_analysis"
),

path(
    "mobile-testing/upload-apk/",
    views.upload_mobile_apk_view,
    name="upload_mobile_apk"
),

path(
    "testing-progress/",
    views.testing_progress,
    name="testing_progress"
),

path(
    "results/",
    views.results_dashboard,
    name="results_dashboard"
),

path(
    "download-pdf/",
    views.download_pdf,
    name="download_pdf"
),
]