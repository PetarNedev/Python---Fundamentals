students_dict = {}
command = input()

while ":" in command:
    data = command.split(":")
    name, ID, course = data[0], data[1], data[2]
    students_dict[name] = {}
    students_dict[name][ID] = course
    command = input()

searched_course = ' '.join(command.split("_"))

for el in students_dict:
    if searched_course in students_dict.get(el).values():
        for idx in students_dict.get(el):
            print(f"{el} - {idx}")
