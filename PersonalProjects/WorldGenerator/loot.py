
def loot(challenge):

    easy = {
        "Common": 62.5,
        "Uncommon": 20,
        "Rare": 10,
        "Legendary": 5,
        "Mythical": 2.5
    }

    normal = {
        "Common": 49.4,
        "Uncommon": 18.8,
        "Rare": 13.1,
        "Legendary": 10.6,
        "Mythical": 8.1
    }

    hard = {
        "Common": 36.3,
        "Uncommon": 17.5,
        "Rare": 16.3,
        "Legendary": 16.3,
        "Mythical": 13.8
    }

    challenging = {
        "Common": 23.1,
        "Uncommon": 16.3,
        "Rare": 19.4,
        "Legendary": 21.9,
        "Mythical": 19.4
    }

    lethal = {
        "Common": 10,
        "Uncommon": 15,
        "Rare": 22.5,
        "Legendary": 27.5,
        "Mythical": 25
    }

    if challenge <= 43:
        return  easy, "Easy"
    elif challenge <= 57:
        return  normal, "Normal"
    elif challenge <= 71:
        return  hard, "Hard"
    elif challenge <= 85:
        return  challenging, "Challenging"
    elif challenge <= 100:
        return lethal, "Lethal"
    else:
        return 'None'