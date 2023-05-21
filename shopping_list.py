shopping_list = input().split("!")

while True:
    line = input()
    if line == "Go Shopping!":
        break

    command = line.split()[0]
    item = line.split()[1]

    if command == "Urgent":
        if item in shopping_list:
            continue
        else:
            shopping_list.insert(0, item)

    elif command == "Unnecessary":
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            continue

    elif command == "Correct":
        if item in shopping_list:
            old_idx = shopping_list.index(item)
            shopping_list.pop(old_idx)
            new_item = line.split()[2]
            shopping_list.insert(old_idx, new_item)
        else:
            continue

    elif command == "Rearrange":
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)
        else:
            continue

print(', '.join(shopping_list))
