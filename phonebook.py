phone_contact = {}
n = 0
while True:
    line = input()
    parts = line.split("-")
    if len(parts) == 1:
        n = int(line)
        break
    name = parts[0]
    number = parts[1]

    phone_contact[name] = number

for i in range(n):
    name = input()
    if name in phone_contact:
        print(f"{name} -> {phone_contact[name]}")
    else:
        print(f"Contact {name} does not exist.")

