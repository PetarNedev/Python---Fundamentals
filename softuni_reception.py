first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students = int(input())

hour = 0
students_per_hour = first_employee + second_employee + third_employee

while students > 0:
    hour += 1
    students -= students_per_hour

    if hour % 4 == 0:
        hour += 1

    if students <= 0:
        break

if hour == 0:
    print(f"Time needed: 0h.")
else:
    print(f"Time needed: {hour}h.")
