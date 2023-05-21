def odd_even_sum(num):
    odd = 0
    even = 0
    for num in number:
        num = int(num)
        if num % 2 == 0:
            even += num
        else:
            odd += num
    return f"Odd sum = {odd}, Even sum = {even}"


number = input()

print(odd_even_sum(number))

