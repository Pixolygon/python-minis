# dad joke 9001
from pyfiglet import figlet_format as fig
from termcolor import colored
from colorama import init
import requests
from random import choice

# use colorama to make colours work on windows
init()

intro = "Dad Joke 9001"
intro_color = "cyan"
intro_final = colored(fig(intro), intro_color)

print(intro_final)


topic = input("Have I got a joke for you!\nGimme a topic, any topic: ")
url = "https://icanhazdadjoke.com/search"
response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": topic}
).json()

total = response["total_jokes"]
results = response["results"]

if total == 0:
    print(f"Sorry, there are {total} jokes about {topic}.")
else:
    print(
        f"There are {total} jokes for {topic}. Here's one:\n"
        + choice(results)["joke"]
    )
