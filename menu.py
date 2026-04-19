def categorize_places():
    while True:
        places = input("\nType the place (or 'menu'): ").lower()

        if places == "menu":
            print("Back to menu")
            break

        familiar = ["home", "office", "bakery", "677 street", "vizzoto street", "restaurant", "grocery", "grocery store" ]
        unfamiliar = ["clinic", "mall", "shop", "shopping", "hospital", "andrade street", "231 street", "354 street", "564 street"]

        if places in unfamiliar:
            print("Unfamiliar")
        elif places in familiar:
            print("Familiar")
        else:
            print("Not informed in database")

while True:
    print("\nMENU)")
    print("1 - Categorize Place")
    print("2 - Close")

    x = input("Type 1 ou 2: ")

    if x == "1":
        categorize_places()
        

    elif x == "2":
        break

    else:
        print("Invalid")