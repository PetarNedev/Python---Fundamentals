text = input()
digits = ""
letter = ""
other = ""

for ch in text:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letter += ch
    else:
        other += ch
print(digits)
print(letter)
print(other)
