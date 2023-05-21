def calculation(a, operator, b):
    result = 0
    if operator == "*":
        result = a * b
    elif operator == "/":
        result = a // b
    elif operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    return result


first_number = int(input())
input_operator = input()
second_number = int(input())

print(calculation(first_number, input_operator, second_number))
