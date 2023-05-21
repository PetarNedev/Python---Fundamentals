line = int(input())
students_grade = {}
for i in range(line):
    key = input()
    value = float(input())

    if key in students_grade:
        students_grade[key].append(value)
    else:
        students_grade[key] = []
        students_grade[key].append(value)

for el in students_grade:
    average_sum = sum(students_grade[el]) / len(students_grade[el])
    if average_sum >= 4.50:
        print(f"{el} -> {average_sum:.2f}")
