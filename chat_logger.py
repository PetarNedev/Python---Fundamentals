chat_list = []
while True:
    command = input().split()
    if command[0] == "end":
        break

    if command[0] == "Chat":
        chat_list.append(command[1])

    if command[0] == "Delete":
        if command[1] in chat_list:
            idx = chat_list.index(command[1])
            chat_list.pop(idx)
        else:
            continue

    if command[0] == "Edit":
        if command[1] in chat_list:
            idx = chat_list.index(command[1])
            chat_list.pop(idx)
            chat_list.insert(idx, command[2])
        else:
            continue

    if command[0] == "Pin":
        if command[1] in chat_list:
            chat_list.remove(command[1])
            chat_list.append(command[1])
        else:
            continue

    if command[0] == "Spam":
        for el in command:
            chat_list.append(el)
        if command[0] in chat_list:
            chat_list.remove(command[0])

print('\n'.join(chat_list))
