
"""
Takes the seed as a list of 7 digits. Looks at the first 3 and depending on the value, selects
the datapoint from the list. These are returned as a dictionary
"""


def layout(seed_list):
    check_size = seed_list[0]
    check_depth = seed_list[1]
    check_special = seed_list[2]
    results = {
        "Size": (0, 0),
        "Depth": 0,
        "Special": ""
    }

    Size = [
        (50, 50),
        (75, 75),
        (100, 100),
        (125, 125),
        (150, 150),
        (200, 200),
        (250, 250),
        (300, 300),
        (400, 400),
        (500, 500)
    ]

    Depth = [
        30,
        40,
        50,
        60,
        70,
        80,
        100,
        120,
        140,
        160
    ]

    Special = [
        "Islands",
        "Mountains",
        "Ravines",
        "Freshwater",
        "Saltwater",
        "Volcano",
        "Ice caps",
        "Desert",
        "Crash-zone",
        "Tundra"
    ]

    results["Size"] = Size[check_size]
    results["Depth"] = Depth[check_depth]
    results["Special"] = Special[check_special]

    return results