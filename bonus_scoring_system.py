from math import ceil
students = int(input())
lecture = int(input())
bonus = int(input())

bonus_list = []
for i in range(students):
    lines = int(input())
    bonus_list.append(lines)

if len(bonus_list) > 0:
    max_number = max(bonus_list)
    total_bonus = max_number / lecture * (5 + bonus)
    print(f"Max Bonus: {ceil(total_bonus)}.")
    print(f"The student has attended {max_number} lectures.")
else:
    print(f"Max Bonus: 0.")
    print(f"The student has attended 0 lectures.")
    