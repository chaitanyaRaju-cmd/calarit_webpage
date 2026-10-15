import requests

import time

from bs4 import BeautifulSoup


def analyze_performance(url):

    try:

        start_time = time.time()

        response = requests.get(
            url,
            timeout=15
        )

        end_time = time.time()

        load_time = round(
            end_time - start_time,
            2
        )

        page_size = round(
            len(response.content) / 1024,
            2
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        images = len(
            soup.find_all("img")
        )

        scripts = len(
            soup.find_all("script")
        )

        score = 100

        if load_time > 3:
            score -= 20

        if page_size > 2048:
            score -= 20

        if images > 50:
            score -= 10

        if scripts > 30:
            score -= 10

        return {

            "status": "PASS",

            "load_time": load_time,

            "page_size": page_size,

            "images": images,

            "scripts": scripts,

            "score": score

        }

    except Exception:

        return {

            "status": "FAIL",

            "load_time": 0,

            "page_size": 0,

            "images": 0,

            "scripts": 0,

            "score": 0

        }