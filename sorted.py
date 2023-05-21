def sorted_num(numbers):
    return sorted(numbers)


some_numbers = [round(float(x)) for x in input().split()]

print(sorted_num(some_numbers))
