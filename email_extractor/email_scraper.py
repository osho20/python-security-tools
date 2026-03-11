import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests
import re

url = "https://example.com"

response = requests.get(url, verify=False)

emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", response.text)

for email in emails:
    print(email)
with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")