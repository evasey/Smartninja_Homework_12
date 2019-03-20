

#A local gaming company contacted you to build a game for them.
#  It is a simple geography quiz where a user has to guess the capital city of some country:


        
#import der benötigten Python Funktionen
import random #Software-Paket
import json #Software-Bibliothek
import datetime
# -*- coding: utf-8 -*-

geo_liste = {"Austria": "Vienna",
                    "China": "Peking",
                    "Croatia": "Zagreb",
                    "Germany": "Berlin",
                    "Namibia": "Windhoek",
                    "Spain": "Madrid",
                    "Switzerland": "Bern",
                    "Italy": "Rome"
                    }
attempts = 0
land, hauptstadt = random.choice(list(geo_liste.items()))

while True:
    attempts += 1
    guess = input(f"What is the capital city of {land} ?")

    if hauptstadt == guess:
        print("Right")
        print(f"You had {attempts} attempts.")
        break
    else:
        print("That's wrong. Please try again.")

