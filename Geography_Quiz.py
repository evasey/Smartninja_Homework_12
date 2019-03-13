#A local gaming company contacted you to build a game for them.
#  It is a simple geography quiz where a user has to guess the capital city of some country:


import random

countries_cities = {"Austria": "Vienna",
                    "China": "Peking",
                    "Croatia": "Zagreb",
                    "Germany": "Berlin",
                    "Namibia": "Windhoek",
                    "Spain": "Madrid",
                    "Switzerland": "Bern",
                    "Italy": "Rome"
                    }

while True:
    random = random.choice(list(countries_cities))
    question = input ("What is the capital city of " + random + "?")
    if countries_cities.values() == question:
        print("This is correct!")
        break
    else:
       print("That's wrong!")


