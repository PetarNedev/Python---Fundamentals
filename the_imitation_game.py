message = input()
# massage_dict = []
# for i in massage:
#     massage_dict.append(i)
moved_letters = ""


while True:
    command = input().split("|")
    if command == ["Decode"]:
        break
    if command[0] == "Move":
        number_of_letters = int(command[1])
        # for el in range(number_of_letters):
        message = message[number_of_letters:] + message[:number_of_letters]

    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        # massage_dict.insert(index, value)
        message = message[:index] + value + message[index:]

    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        # for idx in massage_dict:
        #     if idx == substring:
        #         substring_index = massage_dict.index(idx)
        #         massage_dict.pop(substring_index)
        #         massage_dict.insert(substring_index, replacement)
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")
