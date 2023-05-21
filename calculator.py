def add(a, b):
    result = a + b
    return result


def subtract(a, b):
    result = a - b
    return result


def divide(a, b):
    result = a / b
    return result


def multiply(a, b):
    result = a * b
    return result


first_number = int(input())
operator = input()
second_number = int(input())

if operator == "+":
    print(add(first_number, second_number))
elif operator == "-":
    print(subtract(first_number, second_number))
elif operator == "/":
    print(divide(first_number, second_number))
elif operator == "*":
    print(multiply(first_number, second_number))



