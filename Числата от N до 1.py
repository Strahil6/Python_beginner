def numbers():
    input_number = int(input("Enter number: "))

    for i in reversed(range(input_number, 0)):
        print(i)

numbers()