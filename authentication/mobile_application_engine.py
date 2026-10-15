import os
from datetime import datetime

from androguard.core.apk import APK


def validate_uploaded_apk(apk_path):
    """
    Validate the uploaded APK.
    """

    if not apk_path:
        return False, "No APK path provided."

    if not os.path.exists(apk_path):
        return False, "Uploaded APK not found."

    if not apk_path.lower().endswith(".apk"):
        return False, "Uploaded file is not an APK."

    if os.path.getsize(apk_path) == 0:
        return False, "Uploaded APK is empty."

    return True, "APK validation successful."


def extract_apk_file_information(apk_path):
    """
    Extract basic information about the uploaded APK file.
    """

    file_size = os.path.getsize(apk_path)

    created_time = datetime.fromtimestamp(
        os.path.getctime(apk_path)
    )

    modified_time = datetime.fromtimestamp(
        os.path.getmtime(apk_path)
    )

    return {

        "file_name": os.path.basename(apk_path),

        "file_size_bytes": file_size,

        "file_size_mb": round(
            file_size / (1024 * 1024),
            2
        ),

        "created_time": created_time.strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "modified_time": modified_time.strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    }

def extract_apk_metadata(apk_path):
    """
    Extract Android application metadata from the APK.
    """

    apk = APK(apk_path)

    return {

        "package_name": apk.get_package(),

        "application_name": apk.get_app_name(),

        "version_name": apk.get_androidversion_name(),

        "version_code": apk.get_androidversion_code(),

        "min_sdk_version": apk.get_min_sdk_version(),

        "target_sdk_version": apk.get_target_sdk_version()

    }

def extract_apk_permissions(apk_path):
    """
    Extract all permissions requested by the APK.
    """

    apk = APK(apk_path)

    permissions = apk.get_permissions()

    return sorted(permissions)

def extract_apk_components(apk_path):
    """
    Extract Android application components.
    """

    apk = APK(apk_path)

    return {

        "activities": apk.get_activities(),

        "services": apk.get_services(),

        "receivers": apk.get_receivers(),

        "providers": apk.get_providers()

    }

def extract_apk_certificate(apk_path):
    """
    Extract APK certificate information.
    """

    apk = APK(apk_path)

    certificates = apk.get_certificates()

    if not certificates:

        return {

            "available": False,

            "message": "Certificate not found."

        }

    certificate = certificates[0]

    return {

        "available": True,

        "issuer": str(certificate.issuer),

        "subject": str(certificate.subject),

        "serial_number": str(certificate.serial_number),

        "signature_algorithm": str(
           certificate.signature_algo
        )

    }

def analyze_mobile_application(apk_path):

    print("\n========== CALARIT MOBILE APPLICATION ENGINE ==========")

    """
    CALARIT Mobile Application Engine

    Public function for APK analysis.
    """

    is_valid, message = validate_uploaded_apk(apk_path)

    if not is_valid:

        return {

            "success": False,

            "engine": "Mobile Application Engine",

            "message": message

        }

    apk_information = extract_apk_file_information(
        apk_path
    )

    apk_metadata = extract_apk_metadata(
        apk_path
    )

    apk_permissions = extract_apk_permissions(
        apk_path
    )

    apk_components = extract_apk_components(
    apk_path
)
    
    apk_certificate = extract_apk_certificate(
    apk_path
)

    print("APK Information:")
    print(apk_information)

    print("\nAPK Metadata:")
    print(apk_metadata)

    print("\nPermissions:")
    print(apk_permissions)

    print("\nComponents:")
    print(apk_components)

    print("\nCertificate:")
    print(apk_certificate)

    return {

        "success": True,

        "engine": "Mobile Application Engine",

        "message": message,

        "application_analysis": {

            "apk_information": apk_information,

            "apk_metadata": apk_metadata,

            "permissions": apk_permissions,

            "components": apk_components,

            "certificate": apk_certificate,

        }

    }