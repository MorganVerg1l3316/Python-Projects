from layout import layout
from loot import loot
from difficulty import difficulty

def main(seed):
    if not isinstance(seed, str):
        raise ValueError("Seed must be inputted as a String")
    seed_list = [int(character) for character in seed]
    terrain = layout(seed_list) #Will return the layout
    gear, difficulty_name =  loot(difficulty(terrain)) #Will give gear rarities and the difficulty

    print("Layout =", terrain)
    print("Difficulty =", difficulty_name)
    print("loot rarities on this difficulty")

    for rarity, chance in gear.items():
        print(f" {rarity}: {chance}%")

main("1234567")














