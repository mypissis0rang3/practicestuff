def class_item(item):
    item = item.lower()

    familiar=["house", "bakery"]
    unfamiliar=["clinic", "office"]

    if item in familiar:
        return "Familiar"
    elif item in unfamiliar:
        return "Unfamiliar"
    else:
        return "Not informed in database"
    
print(class_item("fsdsdfsd"))
