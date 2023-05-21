number = int(input())
word = input()
strings = []
filtered_strings = []
for i in range(number):
    current_strings = input()
    strings.append(current_strings)
    if word in current_strings:
        filtered_strings.append(current_strings)
print(strings)
print(filtered_strings)

