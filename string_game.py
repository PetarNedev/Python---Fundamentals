text = input()
while True:
    command = input().split()

    if command == ["Done"]:
        break

    if command[0] == "Change":
        char = command[1]
        replacement = command[2]
        if char in text:
            text = text.replace(char, replacement)
            print(text)
        else:
            print(text)

    elif command[0] == "Includes":
        substring = command[1]
        if substring in text:
            print("True")
        else:
            print("False")

    elif command[0] == "End":
        end_substring = command[1]
        if text[::-1] != end_substring:
            print("False")
        else:
            print("True")

    elif command[0] == "Uppercase":
        text = text.upper()
        print(text)

    elif command[0] == "FindIndex":
        index_char = command[1]
        for el in text:
            if index_char == el:
                index = text.index(el)
                print(index)
                break

    elif command[0] == "Cut":
        start_index = int(command[1])
        count = int(command[2])
        first_cut = text[start_index:]
        second_cut = first_cut[:count]
        print(second_cut)

