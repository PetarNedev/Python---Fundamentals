my_dict = {}
while True:
    key = input()
    if key == "stop":
        break
    value = int(input())

    if key in my_dict:
        my_dict[key] += value
    else:
        my_dict[key] = value

for el in my_dict:
    print(f"{el} -> {my_dict[el]}")

