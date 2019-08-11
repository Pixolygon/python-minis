# Tells a user how many years, and in what year, they will turn a given age.

import datetime

usr = input('What is your name?: ')
curr_age = int(input('How old are you?: '))
future_age = int(input('Enter future age: '))
curryear = datetime.datetime.now().year

print(f'{usr.capitalize()}, you will turn {future_age} in {curryear + (future_age - curr_age)}, {future_age - curr_age} years from now.')
