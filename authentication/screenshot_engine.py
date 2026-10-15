import os
import time
from datetime import datetime
from urllib.parse import urlparse

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager


def capture_screenshot(url):

    try:

        screenshots_dir = os.path.join(
            "media",
            "screenshots"
        )

        os.makedirs(
            screenshots_dir,
            exist_ok=True
        )

        domain = urlparse(url).netloc

        domain = (
            domain.replace("www.", "")
            .replace(".", "_")
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        file_name = (
            f"{domain}_{timestamp}.png"
        )

        screenshot_path = os.path.join(
            screenshots_dir,
            file_name
        )

        chrome_options = Options()

        chrome_options.add_argument(
            "--headless=new"
        )

        chrome_options.add_argument(
            "--window-size=1920,1080"
        )

        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            ),
            options=chrome_options
        )

        driver.get(url)

        time.sleep(3)

        driver.save_screenshot(
            screenshot_path
        )

        driver.quit()

        return (
            "/media/screenshots/"
            + file_name
        )

    except Exception as e:

        print(
            "Screenshot Error:",
            e
        )

        return None