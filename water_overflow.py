lines = int(input())
tank = 0
for i in range(lines):
    command = input()
    liters = int(command)
    tank += liters
    if tank > 255:
        tank -= liters
        print("Insufficient capacity!")
        continue
print(tank)
