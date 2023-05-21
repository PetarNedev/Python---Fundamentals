def absolute_values(num):
    my_list = []
    for num in numbers:
        my_list.append(abs(float(num)))
    return my_list


numbers = input().split()

print(absolute_values(numbers))
