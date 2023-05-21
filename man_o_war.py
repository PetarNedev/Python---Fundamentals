pirate_ship = [int(x) for x in input().split(">")] # 12>13>11>20>66
warship = [int(x) for x in input().split(">")] # 12>22>33>44>55>32>18
health = int(input())
ship_is_sunken = False
while True:
    line = input().split()
    if line == "Retire":
        break
    command = line[0]
    idx = int(line[1])

    if command == "Fire":
        if idx <= len(warship):
            warship[idx] = warship[idx] - int(line[2])
        if warship[idx] <= 0:
            print("You won! The enemy ship has sunken.")
            break
        else:
            continue

    elif command == "Defend":
        start_index = idx
        end_index = int(line[2])
        damage = int(line[3])
        if start_index >= 0 and end_index <= len(pirate_ship):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    break
            ship_is_sunken = True
        if ship_is_sunken:
            break
        else:
            continue

    elif command == "Repair":
        pass
    elif command == "Status":
        pass


