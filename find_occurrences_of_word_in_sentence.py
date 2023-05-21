import re

text = input().lower()
target = input().lower()
regex = f"\\b{target}\\b"
matches = re.findall(regex, text)
print(len(matches))
