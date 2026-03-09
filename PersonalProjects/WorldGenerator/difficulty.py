

def difficulty(layout):
    count = 0

    if layout.get("Size") == [50,50] or [75.75] or [100,100]:
        count += 5
    elif layout.get("Size") == [125,125] or [150, 150] or [200,200]:
        count += 15
    elif layout.get("Size") == [250,250] or [300,300] or [400,400]:
        count += 25
    else:
        count += 35


    if layout.get("Depth") == 30 or 40 or 50:
        count += 5
    elif layout.get("Depth") == 60 or 70 or 80:
        count += 10
    elif layout.get("Depth") == 100 or 120 or 140:
        count += 15
    else:
        count += 20

    if layout.get("Special") == "Islands" or "Freshwater" or "Mountains":
        count += 10
    elif layout.get("Special") == "Saltwater" or "Desert" or "Ravenes":
        count += 20
    elif layout.get("Special") == "Volcano" or "Ice caps" or "Tundra":
        count += 30
    else:
        count += 45


    return count
