numbers = input().split(", ")
zero_list = []
number_list = []
for i in numbers:
    i = int(i)
    if i == 0:
        zero_list.append(i)
    else:
        number_list.append(i)

print(number_list + zero_list)
