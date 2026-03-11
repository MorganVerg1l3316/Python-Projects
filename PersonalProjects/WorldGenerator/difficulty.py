"""
Takes the dictionary from the layout. We have 3 dictionaries for each aspect of the terrain.
It increments the difficulty score depending on which element came up from the seed in the prior method.
The total number from this is returned as the difficulty number
"""



def difficulty(layout):
    count = 0

    size_scores = {
        (50,50): 5, (75,75): 5, (100,100): 5,
        (125,125): 15, (150,150): 15, (200,200): 15,
        (250,250): 25, (300,300): 25, (400,400): 25
    }


    depth_scores = {
        30: 5, 40: 5, 50: 5,
        60: 10, 70: 10, 80: 10,
        100: 15, 120: 15, 140: 15
    }


    special_scores = {
        "Islands": 10, "Freshwater": 10, "Mountains": 10,
        "Saltwater": 20, "Desert": 20, "Ravines": 20,
        "Volcano": 30, "Ice caps": 30, "Tundra": 30
    }

    count += size_scores.get(layout["Size"], 35)
    count += depth_scores.get(layout["Depth"], 20)
    count += special_scores.get(layout["Special"], 45)

    return count
