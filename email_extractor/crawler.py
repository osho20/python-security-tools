import requests
from bs4 import BeautifulSoup
import re

start_url = "https://example.com"

visited = set()
emails_found = set()

def crawl(url):

    if url in visited:
        return

    visited.add(url)

    try:
        response = requests.get(url, verify=False)
    except:
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # find emails
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", response.text)

    for email in emails:
        emails_found.add(email)

    # find links
    links = soup.find_all("a")

    for link in links:
        href = link.get("href")

        if href and href.startswith("http"):
            crawl(href)

crawl(start_url)

for email in emails_found:
    print(email)
with open("emails_found.txt","w") as file:
    for email in emails_found:
        file.write(email + "\n")