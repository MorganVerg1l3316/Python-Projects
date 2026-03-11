"""
This function takes the difficulty name and the seed. The difficulty is used to decide which pool of enemy
types is used. The harder pools have the challenging enemies and vice versa. Then we search that pool
for the difficulty in the parameter and the challenge number from it. We then move those enemy types into a list.
The last four digits of the seed are added together and that number is used in the calculation of which enemy
is selected from the list. We then return a string of that enemy faction.
"""

import random
# from collections import Counter

def factions(difficulty,seed):

    last_four = seed[-4:]
    faction_number = sum(last_four)

    challenge = 0

    if difficulty == "easy":
        challenge = 1
    elif difficulty == "normal":
        challenge = 2
    elif difficulty in ("hard", "challenging"):
        challenge = 3
    elif difficulty == "lethal":
        challenge = 4

    enemies = {
        "easy": ("Orcs","Trolls","Dark Elves"),
        "normal": ("Orcs", "Trolls", "Dark Elves", "Mind-flayers", "Dark-knights"),
        "hard": ("Mind-flayers", "Dark-knights", "empire"),
        "secret": "empire"

    }

    easy = []
    normal = []
    hard = []
    secret = []

    for key, value in enemies.items():
        if challenge == 1 and key == "easy":
            easy.extend(value)
        elif challenge == 2 and key == "normal":
            normal.extend(value)
        elif challenge == 3 and key == "hard":
            hard.extend(value)
        elif challenge == 4 and key == "secret":
            secret.extend(value)

    chosen_faction = ""

    if easy:
        chosen_faction = easy[faction_number % len(easy)]
    elif hard:
        chosen_faction = hard[faction_number % len(hard)]
    elif normal:
        chosen_faction = normal[faction_number % len(normal)]
    elif secret:
        chosen_faction = "empire"
    else:
        print("Error in difficulty lists")

    return chosen_faction




