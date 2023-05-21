my_list = [int(x) for x in input().split()]
new_list = []

while True:
    command = input().split()

    if command == ["end"]:
        break

    new_command = command[0]

    if new_command == "swap":
        first_index = int(command[1])
        second_index = int(command[2])
        my_list[first_index], my_list[second_index] = my_list[second_index], my_list[first_index]

    elif new_command == "multiply":
        first_index = int(command[1])
        second_index = int(command[2])
        result = my_list[first_index] * my_list[second_index]
        my_list.pop(first_index)
        my_list.insert(first_index, result)

    elif new_command == "decrease":
        for el in my_list:
            el -= 1
            new_list.append(el)

converted_list = map(str, new_list)
print(', '.join(converted_list))
