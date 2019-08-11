from pyfiglet import figlet_format as fig
from termcolor import colored
from colorama import init

# use colorama to make colours work on windows
init()

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

msg = input("What would you like to say? ")
print("\nred, green, yellow, blue, magenta, cyan, white")
color = input("What colour? ")

if color not in valid_colors:
    color = "magenta"

ascii_msg = fig(msg)
colored_ascii = colored(ascii_msg, color)

print(colored_ascii)
