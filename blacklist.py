friends = input().split(", ")
blacklisted = 0
lost_name = 0
while True:
    command = input().split()
    if command[0] == "Report":
        break

    if command[0] == "Blacklist":
        if command[1] in friends:
            blacklisted += 1
            print(f"{command[1]} was blacklisted.")
            idx_of_friend = friends.index(command[1])
            friends.pop(idx_of_friend)
            friends.insert(idx_of_friend, "Blacklisted")
        else:
            print(f"{command[1]} was not found.")

    if command[0] == "Error":
        if 0 <= int(command[1]) < len(friends):
            if friends[int(command[1])] == "Blacklisted" or friends[int(command[1])] == "Lost":
                continue

            else:
                print(f"{friends[int(command[1])]} was lost due to an error.")
                friends.pop(int(command[1]))
                friends.insert(int(command[1]), "Lost")
                lost_name += 1

    if command[0] == "Change":
        if 0 <= int(command[1]) < len(friends):
            print(f"{friends[int(command[1])]} changed his username to {command[2]}.")
            friends.pop(int(command[1]))
            friends.insert(int(command[1]), command[2])

        else:
            continue

print(f"Blacklisted names: {blacklisted}")
print(f"Lost names: {lost_name}")
print(' '.join(friends))
