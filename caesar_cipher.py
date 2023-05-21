text = input()

for i in text:
    for letter in i:
        number_of_letter = ord(letter) + 3
        print(chr(number_of_letter), end="")

