license_dict = {}

line = int(input())

for _ in range(line):
    command_info = input().split()
    command = command_info[0]
    name = command_info[1]

    if command == "register":
        license_plate = command_info[2]
        if name in license_dict:
            print(f"ERROR: already registered with plate number {license_dict[name]}")
        else:
            license_dict[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
    else:
        if name in license_dict:
            license_dict.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for name, license_plate in license_dict.items():
    print(f"{name} => {license_plate}")
