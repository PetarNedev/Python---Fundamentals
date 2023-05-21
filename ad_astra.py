import re
text = input()

pattern = r"(?P<Item>[A-z]+)(?P<Separator>#|\|)(?P<Date>\d+\/\d+\/\d+)(?P<Separator2>#|\|)(?P<Calories>\d+)"
matches = list(re.findall(pattern, text))
my_list = []
for el in matches:
    for i in el:
        my_list.append(i)
for item in my_list:
    if item == "#" or item == "|":
        idx = my_list.index(item)
        matches = my_list.pop(idx)



print(my_list)

