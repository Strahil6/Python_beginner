def fishingBoat():
    group_budget = int(input("Въведете бюджет: "))
    seasson = input("Въведете сезон: ")
    number_fishermen = int(input("Въведете броя рибари: "))
    price = 0

    if seasson == "Spring":
        price = 3000
        if number_fishermen <= 6:
            price -= price * 0.10
        elif number_fishermen >= 7 and number_fishermen <= 11:
            price -= price * 0.15
        elif number_fishermen >= 12:
            price -= price * 0.25
        
        if number_fishermen % 2 == 0:
            price -= price * 0.05

    elif seasson == "Summer":
        price = 4200
        if number_fishermen <= 6:
            price -= price * 0.10
        elif number_fishermen >= 7 and number_fishermen <= 11:
            price -= price * 0.15
        elif number_fishermen >= 12:
            price -= price * 0.25
        
        if number_fishermen % 2 == 0:
            price -= price * 0.05

    elif seasson == "Autumn":
        price = 4200
        if number_fishermen <= 6:
            price -= price * 0.10
        elif number_fishermen >= 7 and number_fishermen <= 11:
            price -= price * 0.15
        elif number_fishermen >= 12:
            price -= price * 0.25

    elif seasson == "Winter":
        price = 2600
        if number_fishermen <= 6:
            price -= price * 0.10
        elif number_fishermen >= 7 and number_fishermen <= 11:
            price -= price * 0.15
        elif number_fishermen >= 12:
            price -= price * 0.25
        
        if number_fishermen % 2 == 0:
            price -= price * 0.05

    if group_budget >= price:
        left_money = group_budget - price
        print(f"Yes! You have {left_money: .2f} leva left.")
    else:
        need_money = price - group_budget
        print(f"Not enough money! You need {need_money: .2f} leva.")
fishingBoat()