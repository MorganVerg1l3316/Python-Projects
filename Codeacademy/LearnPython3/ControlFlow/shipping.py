# Shipping company


def package_weight():
    global weight
    weight = input('How much does the package weigh?   ')
    weight = int(weight)
    return weight


def shipping_type_selection():
    global ship_type
    ship_type = input('''Which type of shipping would you like?
    Ground, Premium or Drone?   ''')
    return ship_type


def weight_calc():
    shipping_type_selection()
    while ship_type == 'ground' or 'Ground':
        if weight <= 2:
            price_per = 1.5
            flat = 20
            total = ((price_per * weight) + flat)
            print(f"Your total is {total}")
            break
        elif weight > 2 and weight <= 6:
            price_per = 3.0
            flat = 20
            total = ((price_per * weight) + flat)
            print(f"Your total is {total}")
            break
    while ship_type == 'Premium' or 'premium':
        if weight <= 2:
            price_per = 1.5
            flat = 125
            total = ((price_per * weight) + flat)
            print(f"Your total is {total}")
            break


def main():
    package_weight()
    weight_calc()


main()
