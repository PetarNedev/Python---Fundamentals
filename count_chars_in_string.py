text = input().split()
my_dict = {}
value = 0
for i in text:
    for ch in i:
        if ch not in my_dict:
            my_dict[ch] = value
        if ch in my_dict:
            my_dict[ch] += 1

for el in my_dict:
    print(f"{el} -> {my_dict[el]}")
