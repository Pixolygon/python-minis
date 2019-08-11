# http://books.toscrape.com/catalogue/category/books/horror_31/index.html
import sqlite3
import requests
from bs4 import BeautifulSoup as bs

url = "http://books.toscrape.com/catalogue/category/books/horror_31/index.html"


def scrape_books(url):
    res = requests.get(url)
    soup = bs(res.text, "html.parser")
    books = soup.find_all("article")
    all_books = []
    for book in books:
        book_data = (get_title(book), get_price(book), get_rating(book))
        all_books.append(book_data)
    save_books(all_books)


def get_title(book):
    return book.find("h3").find("a")['title']


def get_price(book):
    price = book.select('.price_color')[0].get_text()
    return float(price.replace("£", "").replace("Â", ""))


def get_rating(book):
    stars = book.select(".star-rating")[0]
    word_to_int = {"Zero": 0, "One": 1, "Two": 2,
                   "Three": 3, "Four": 4, "Five": 5}
    rating_word = stars.get_attribute_list("class")[-1]
    return word_to_int[rating_word]


def save_books(all_books):
    con = sqlite3.connect("scrape_to_db.db")
    c = con.cursor()
    c.execute('''
        CREATE TABLE books (title TEXT, rating INTEGER, price REAL)
        ''')
    c.executemany("INSERT INTO books VALUES (?,?,?)", all_books)
    con.commit()
    con.close()


scrape_books(url)
