def cinema():
    projectType = input("Enter type project: ")
    row = int(input("Enter number row: "))
    col = int(input("Enter number col: "))
    price = 0

    if projectType == "Premiere":
        price = row * col * 12
    elif projectType == "Normal":
        price = row * col * 7.50
    elif projectType == "Discount":
        price = row * col * 5

    print("%.2f leva" % price)

cinema()