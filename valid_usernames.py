from string import ascii_letters, digits

words = input().split(", ")
allowed_ch = ascii_letters + digits + "-" + "_"

for word in words:
    if len(word) < 3 or len(word) > 16:
        continue

    forbidden_ch = False
    for ch in word:
        if ch not in allowed_ch:
            forbidden_ch = True
            break
    if forbidden_ch:
        continue

    print(word)
