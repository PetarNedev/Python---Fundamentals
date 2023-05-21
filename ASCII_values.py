# data = input().split(", ")
# my_dict = {}
# for x in data:
#     my_dict[x] = ord(x)
# print(my_dict)

my_dict = {x: ord(x) for x in input().split(", ")}
print(my_dict)
