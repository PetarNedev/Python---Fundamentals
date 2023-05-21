def min_max_sum(num):
    print(f"The minimum number is {min(num)}")
    print(f"The maximum number is {max(num)}")
    print(f"The sum number is: {sum(num)}")


some_numbers = [round(float(x)) for x in input().split()]

min_max_sum(some_numbers)
