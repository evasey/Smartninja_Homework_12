

#A local gaming company contacted you to build a game for them.
#  It is a simple geography quiz where a user has to guess the capital city of some country:


import random  # Software-Paket

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
country, capital = random.choice(list(geo_liste.items()))

while True:
    attempts += 1
    guess = input(f"What is the capital city of {country} ?")

    if capital == guess:
        print("You've guessed it. Congratulations!")
        print(f"You had {attempts} attempts.")
        break
    else:
        print("That's wrong. Please try again.")


