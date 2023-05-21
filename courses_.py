courses_dict = {}

while True:
    command = input().split(" : ")

    if command == ["end"]:
        break
    course = command[0]
    name = command[1]

    if course not in courses_dict:
        courses_dict[course] = []
    if course in courses_dict:
        courses_dict[course].append(name)

for course, students in courses_dict.items():
    print(f"{course}: {len(students)}")
    for students_name in students:
        print(f"-- {students_name}")
