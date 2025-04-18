def hotelRoom():
    month = input("Enter month: ")
    number_of_night = int(input("Enter number of night: "))
    price_for_studio = 0
    price_for_apartment = 0

    if month == "May" or month == "October":
        price_for_studio = number_of_night * 50
        price_for_apartment = number_of_night * 65

        if number_of_night >= 7 and number_of_night <= 14:
            price_for_studio -= price_for_studio * 0.05
        elif number_of_night > 14:
            price_for_studio -= price_for_studio * 0.30
            price_for_apartment -= price_for_apartment * 0.10

    elif month == "June" or month == "September":
        price_for_studio = number_of_night * 75.20
        price_for_apartment = number_of_night * 68.70

        if number_of_night > 14:
            price_for_studio -= price_for_studio * 0.20
            price_for_apartment -= price_for_apartment * 0.10

    elif month == "July" or month == "August":
        price_for_studio = number_of_night * 76
        price_for_apartment = number_of_night * 77

        if number_of_night > 14:
            price_for_apartment -= price_for_apartment * 0.10
    
    print(f"Apartment: {price_for_apartment: .2f} lv")
    print(f"Studio: {price_for_studio: .2f} lv")
hotelRoom()