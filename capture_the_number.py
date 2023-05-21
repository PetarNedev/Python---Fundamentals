import re
result = []
while True:
    pattern = r"\d+"

    text = input()
    if not text:
        break

    matches = re.findall(pattern, text)
    result.extend(matches)

print(' '.join(result))