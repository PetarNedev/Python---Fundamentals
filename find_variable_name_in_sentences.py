import re

text = input()

regex = r"\b_([A-Za-z]+\b)"

matches = re.findall(regex, text)

print(','.join(matches))