def newHouse():
    flower_type = input("Въведете вида на цветята: ")
    number_flower = int(input("Въведете броя на цветята: "))
    budget = int(input("Въведете бюджет: "))
    price = 0

    if flower_type == "Roses":
        price = number_flower * 5
        if number_flower >= 80:
            price -= price * 0.10
    elif flower_type == "Dahlias":
        price = number_flower * 3.80
        if number_flower >= 90:
            price -= price * 0.15
    elif flower_type == "Tulips":
        price = number_flower * 2.80
        if number_flower >= 80:
            price -= price * 0.15
    elif flower_type == "Narcissus":
        price = number_flower * 3
        if number_flower < 120:
            price += price * 0.15
    elif flower_type == "Gladiolus":
        price = number_flower * 2.50
        if number_flower < 80:
            price += price * 0.20

    if budget >= price:
        left_money = budget - price
        print(f"Hey, you have a great garden with {number_flower} {flower_type} and {left_money: .2f} leva left.")
    else:
        need_money = price - budget
        print(f"Not enough money, you need {need_money: .2f} leva more.")

newHouse()