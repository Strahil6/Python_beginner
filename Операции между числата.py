def numberOperation():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    operation = input("Enter operation symbol: ")
    result = 0

    if operation == "+":
        result = first_number + second_number
        if result % 2 == 0:
            print(f"{first_number} + {second_number} = {result} - even")
        else:
            print(f"{first_number} + {second_number} = {result} - odd")

    elif operation == "-":
        result = first_number - second_number
        if result % 2 == 0:
            print(f"{first_number} - {second_number} = {result} - even")
        else:
            print(f"{first_number} - {second_number} = {result} - odd")

    elif operation == "*":
        result = first_number * second_number
        if result % 2 == 0:
            print(f"{first_number} * {second_number} = {result} - even")
        else:
            print(f"{first_number} * {second_number} = {result} - odd")

    elif operation == "/":
        if second_number == 0:
            print(f"Cannot divide {first_number} by zero")
        else:
            result = first_number / second_number
            print(f"{first_number} / {second_number} = {result: .2f}")

    elif operation == "%":
        if second_number == 0:
            print(f"Cannot divide {first_number} by zero")
        else:
            result = first_number % second_number
            print(f"{first_number} % {second_number} = {result}")
numberOperation()