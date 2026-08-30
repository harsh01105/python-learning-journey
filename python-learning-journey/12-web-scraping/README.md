# 12 - Web Scraping

**Book chapter:** Automate the Boring Stuff with Python, 3rd Ed. — Chapter 13

## Notes
- `requests.get(url)` fetches the raw HTML of a webpage.
- `BeautifulSoup(html, "html.parser")` turns that HTML into something you can search through.
- `.find()` gets the first matching element; `.find_all()` gets ALL matching elements.
- You select elements by tag name (`"h1"`, `"a"`) and/or attributes (`class_="price"`, `id="main"`).
- `.text` extracts just the visible text from an element (no HTML tags).
- `.get("href")` extracts an attribute's value (like a link's URL) from a tag.
- Always check a site's `robots.txt` and terms of service before scraping it for real — practice sites like `quotes.toscrape.com` and `books.toscrape.com` exist specifically for learning this safely.