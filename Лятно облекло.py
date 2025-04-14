def summerClothing():
    degree = int(input("Enter degree: "))
    time_of_day = input("Enter time of day: ")
    outfit = ""
    shoes = ""

    if time_of_day == "Morning":
        if degree >= 10 and degree <= 18:
            outfit = "Sweatshirt"
            shoes = "Sneakers"
        elif degree > 18 and degree <= 24:
            outfit = "Shirt"
            shoes = "Moccasins"
        elif degree >= 25:
            outfit = "T-Shirt"
            shoes = "Sandals"
    elif time_of_day == "Afternoon":
        if degree >= 10 and degree <= 18:
            outfit = "Shirt"
            shoes = "Moccasins"
        elif degree > 18 and degree <= 24:
            outfit = "T-Shirt"
            shoes = "Sandals"
        elif degree >= 25:
            outfit = "Swim Suit"
            shoes = "Barefoot"
    elif time_of_day == "Evening":
        if degree >= 10 and degree <= 18:
            outfit = "Shirt"
            shoes = "Moccasins"
        elif degree > 18 and degree <= 24:
            outfit = "Shirt"
            shoes = "Moccasins"
        elif degree >= 25:
            outfit = "Shirt"
            shoes = "Moccasins"

    print(f"It's {degree} degrees, get your {outfit} and {shoes}.")

summerClothing()