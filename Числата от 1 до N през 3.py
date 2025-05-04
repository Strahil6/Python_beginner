def numberBetween1AndN():
    end_number = int(input("Enter number: "))

    for index in range(1, end_number, 3):
        print(index)

numberBetween1AndN()