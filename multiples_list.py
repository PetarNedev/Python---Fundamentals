factor = int(input())
count = int(input())

my_list = []

for i in range(factor, count * factor + 1, factor):
    my_list.append(i)
print(my_list)
