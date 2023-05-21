import re

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

text = input()

match = re.finditer(pattern, text)

for num in match:
    print(num.group(), end=" ")


