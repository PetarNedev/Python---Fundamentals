lines = int(input())
my_dict = {}
for i in range(lines):
    word = input()
    synonym = input()
    if word not in my_dict:
        my_dict[word] = []
    my_dict[word].append(synonym)

for el in my_dict:
    print(f"{el} - {', '.join(my_dict[el])}")
