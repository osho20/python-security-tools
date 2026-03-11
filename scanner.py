import requests
import urllib3
from concurrent.futures import ThreadPoolExecutor

urllib3.disable_warnings()

base_url = "https://example.com"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# read wordlist
with open("wordlist.txt", "r") as file:
    paths = [line.strip() for line in file]


def scan(path):
    url = base_url + "/" + path

    try:
        response = requests.get(url, headers=headers, verify=False, timeout=5)

        if response.status_code == 200:
            print("[FOUND]", url)

    except:
        pass


# run multiple scans at once
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(scan, paths)