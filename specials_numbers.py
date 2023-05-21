number = int(input())

for i in range(1, number + 1):
    special_number = False
    num_as_string = str(i)
    counter = 0
    for ch in num_as_string:
        ch_as_int = int(ch)
        counter += ch_as_int
    if counter == 5 or counter == 7 or counter == 11:
        special_number = True
        print(f"{i} -> {special_number}")
    else:
        print(f"{i} -> {special_number}")
