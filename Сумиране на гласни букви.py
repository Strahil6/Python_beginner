def summationVowelLetters():
    input_word = input("Enter your word: ")
    total = 0

    for index in range(len(input_word)):
        current_digit = input_word[index]

        if current_digit == "a":
            total += 1
        elif current_digit == "e":
            total += 2
        elif current_digit == "i":
            total += 3
        elif current_digit == "o":
            total += 4
        elif current_digit == "u":
            total += 5
    print(total)

summationVowelLetters()