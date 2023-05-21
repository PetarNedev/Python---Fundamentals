def even_numbers(num):
    even = []
    for num in number:
        num = int(num)
        if num % 2 == 0:
            even.append(num)
        else:
            continue
    return even


number = input().split()
print(even_numbers(number))


