"""
This algorithm takes in a seven digit seed as a string. It's converted into a list and those digits are used in various
 areas to return the world. It runs the layout function with the seed, this returns 3 pieces of information:
 A tuple with the x and y for the map, the depth and the biome type. Similar
 to this, the loot function runs the difficulty function with the results of layout.
 This returns the difficulty and the rarities of each loot type on said difficulty. Then it runs the factions
 function which returns the chosen faction.
"""


from layout import layout
from loot import loot
from difficulty import difficulty
from factions import factions
import random
from collections import Counter, defaultdict



def main(seed):
    if not isinstance(seed, str):
        raise ValueError("Seed must be inputted as a String")
    seed_list = [int(character) for character in seed]
    terrain = layout(seed_list) #Will return the layout
    gear, difficulty_name =  loot(difficulty(terrain)) #Will give gear rarities and the difficulty
    enemies = factions(difficulty_name.lower(),seed_list)

    print("Layout =", terrain)
    print("Difficulty =", difficulty_name)
    print("loot rarities on this difficulty")

    for rarity, chance in gear.items():
        print(f" {rarity}: {chance}%")

    print("Faction on this planet: " + enemies.upper())

main("4589276")

# testing factions
# results = Counter()
#
# for _ in range(1000):
#     test_Seed = str(random.randint(1000000, 9999999))
#     faction = factions("lethal",[int(character) for character in test_Seed])
#     results[faction] += 1
#
# print(results)




# testing layouts
# results = Counter()
#
# for _ in range(1000):
#     test_seed = str(random.randint(1000000, 9999999))
#     test_seed_list = [int(character) for  character in test_seed]
#     test_layout = layout(test_seed_list)
#     diff = difficulty(test_layout)
#
#     results[loot(diff)] += 1
#
# print(results)











