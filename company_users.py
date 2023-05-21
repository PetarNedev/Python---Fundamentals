company_users = {}

while True:
    command = input().split(" -> ")
    if command == ["End"]:
        break
    key = command[0]
    value = command[1]

    if key in company_users:
        if value not in company_users.get(key):
            company_users[key].append(value)
    else:
        company_users[key] = []
        company_users[key].append(value)


for company, id_numbers in company_users.items():
    print(f"{company}")
    for el in id_numbers:
        print(f"-- {el}")
