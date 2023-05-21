entry = input().lower().split()
my_dict = {}
value = 0
for el in entry:
    if el not in my_dict:
        my_dict[el] = value
    if el in my_dict:
        my_dict[el] += 1
for el in my_dict:
    if my_dict[el] % 2 != 0:
        print(el, end=" ")
