import csv
import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
OUTPUT_FILE = "scraped_books.csv"

RATING_WORDS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def fetch_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None


def parse_books(html):
    soup = BeautifulSoup(html, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    data = []
    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text.strip()
        rating_class = book.find("p", class_="star-rating")["class"][1]
        rating = RATING_WORDS.get(rating_class, "Unknown")
        data.append({"title": title, "price": price, "rating": rating})
    return data


def save_to_csv(data, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price", "rating"])
        writer.writeheader()
        writer.writerows(data)


def main():
    html = fetch_page(URL)
    if html is None:
        print("Could not fetch data. Exiting.")
        return

    books = parse_books(html)
    save_to_csv(books, OUTPUT_FILE)
    print(f"Saved {len(books)} books to {OUTPUT_FILE}")

    print("\nPreview:")
    for book in books[:5]:
        print(f"{book['title']} | {book['price']} | {book['rating']} stars")


if __name__ == "__main__":
    main()