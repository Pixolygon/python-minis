# http://quotes.toscrape.com
# from time import sleep
from random import choice
import os.path
import json

import requests
from bs4 import BeautifulSoup as bs


fname = "quotes.json"
url = "http://quotes.toscrape.com"


# If fname doesn't exist, scrape and save, else play game
def fcheck(fname):
    if not os.path.isfile(fname):
        scrape()
        game()
    else:
        game()


# Scrape and save
def scrape():
    quotes_storage = []
    page = "/page/1/"
    while page:
        response = requests.get(url + page)
        print(f"Gathering quotes {url}{page}...")
        soup = bs(response.text, "html.parser")
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
            quotes_storage.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "author_url": quote.find("a")['href'],
            })

        more = soup.find(class_="next")
        page = more.find("a")['href'] if more else None
        # sleep(2)
    with open(fname, "w") as f:
        json.dump(quotes_storage, f)


# Get randomized quote from fname
def get_quote():
    with open(fname, "r") as f:
        quote = choice(json.load(f))
        return quote


# Game logic
def game():
    play = 'yes'
    while play.lower() == "y" or play.lower() == "yes":
        quote = get_quote()
        guesses = 4
        guess = ""
        print(quote['text'])
        print(quote['author'])
        while guess.lower() != quote['author'].lower() and 0 < guesses <= 4:
            guess = input(
                f"Who said this? {guesses} guesses remaining.\n")
            if guess.lower() == quote['author'].lower():
                print("\nThat's correct!")
                break
            else:
                guesses -= 1
            if guesses == 3:
                response = requests.get(f"{url + quote['author_url']}")
                soup = bs(response.text, "html.parser")
                born_date = soup.find(class_="author-born-date").get_text()
                born_loc = soup.find(class_="author-born-location").get_text()
                print(
                    f"\nHint: This person was born on {born_date} {born_loc}")
            elif guesses == 2:
                first_initial = quote['author'][0]
                print(f"\nHint: The person's first initial is {first_initial}")
            elif guesses == 1:
                last_initial = quote['author'].split(' ')[1][0]
                print(f"\nHint: The person's last initial is {last_initial}")
            else:
                print(
                    f"\nNo more guesses. The person was {quote['author']}")
        play = ''
        while play.lower() not in ('yes', 'y', 'no', 'n'):
            play = input("Would you like to play again, y/n? ")


# Start the whole thing
fcheck(fname)
