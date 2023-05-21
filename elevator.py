import math

person = int(input())
capacity = int(input())
courses = math.ceil(person / capacity)
print(courses)
