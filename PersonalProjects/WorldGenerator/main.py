from layout import layout
from loot import loot


def main(seed):
    if not isinstance(seed, str):
        raise ValueError("Seed must be inputted as a String")
    seed_list = [int(character) for character in seed]
    terrain = layout(seed_list)
    loot(terrain)










