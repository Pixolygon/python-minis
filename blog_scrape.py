# https://www.rithmschool.com/blog
from bs4 import BeautifulSoup as bs
import requests
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
soup = bs(response.text, "html.parser")
articles = soup.find_all("article")

with open("blog_scrape.csv", "a", newline="") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["date", "title", "url"])

    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag['href']
        date = article.find("time")['datetime']
        csv_writer.writerow([date, title, url])
