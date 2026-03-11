import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://quotes.toscrape.com/page/{}/"

data = []

for page in range(1, 6):

    url = base_url.format(page)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:

        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text

        tags = [tag.text for tag in quote.find_all("a", class_="tag")]
        tags = ", ".join(tags)

        data.append([text, author, tags])

with open("quotes_dataset.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["Quote", "Author", "Tags"])

    writer.writerows(data)

print("Dataset saved successfully.")