def journey():
    budget = float(input("Enter budget: "))
    season = input("Enter season: ")
    destination = ""
    place_of_rest = ""

    if budget <= 100:
        destination = "Bulgaria"
        if season == "Summer":
            budget = budget * 0.30
            place_of_rest = "Camp"
        elif season == "Winter":
            budget = budget * 0.70
            place_of_rest = "Hotel"
    elif budget > 100 and budget <= 1000:
        destination = "Balkans"
        if season == "Summer":
            budget = budget * 0.40
            place_of_rest = "Camp"
        elif season == "Winter":
            budget = budget * 0.80
            place_of_rest = "Hotel"
    elif budget > 1000:
        destination = "Europe"
        place_of_rest = "Hotel"
        budget = budget * 0.90

    print(f"Somewhere in {destination}")
    print(f"{place_of_rest} - {budget: .2f}")
journey()