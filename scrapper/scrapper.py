# Scrapping & Cleaning text from book store

import requests
from bs4 import BeautifulSoup as bs
import json
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"

# Star ratting into number
def get_rating(star_class):
    mapping = {
        "One" : 1,
        "Two" : 2,
        "Three" : 3,
        "Four" : 4,
        "Five" : 5,
    }
    return mapping.get(star_class,0)

# Scrape category
def scrape_category(book_url):
    response = requests.get(book_url)
    soup = bs(response.text, "html.parser")
    breadcrumb = soup.find('ul', class_='breadcrumb')
    category = breadcrumb.find_all('li')[2].text.strip()
    return category

# Scrape pages
def scrape_pages(url):
    response = requests.get(url)
    soup = bs(response.text,"html.parser")
    books = soup.find_all('article',class_='product_pod')

    book_list = []

    for book in books:

        # title scraping
        title = book.h3.a['title']

        # Price
        price = book.find('p',class_='price_color').text.strip().replace('£','')

        # Availability
        availability = book.find('p',class_='instock availability').text.strip()

        # Ratting class
        rating_class = book.find('p')['class'][1]

        # Rating
        rating = get_rating(rating_class)

        detail_url = urljoin(url, book.h3.a['href'])
        category = scrape_category(detail_url)

        # Append all things 
        book_list.append({
            "title":title,
            "price":price,
            "availability":availability,
            "rating":rating,
            "category":category
        })

        return book_list
    
# Scrape all books
def scrape_all_books():
    all_books = []
    page = 1
    while True:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        print(f"Scraping: {url}")
        response = requests.get(url)
        if response.status_code != 200:
            break

        books = scrape_pages(url)
        if not books:
            break

        all_books.extend(books)
        page += 1

    # Save as JSON
    with open("books_clean.json", "w", encoding="utf-8") as f:
        json.dump(all_books, f, indent=2, ensure_ascii=False)

    print(f"\nScraped {len(all_books)} books and saved to 'books_clean.json'")

if __name__ == "__main__":
    scrape_all_books()

