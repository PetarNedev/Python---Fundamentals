new_followers = {}
likes = {}
comments = {}
blocked = {}
followers = 0
while True:
    command = input().split(": ")

    if command == ["Log out"]:
        break
    username = command[1]

    if command[0] == "New follower":
        if username not in new_followers:
            followers += 1
            new_followers[username] = 0

    elif command[0] == "Like":
        count = int(command[2])
        if username not in new_followers:
            followers += 1
            new_followers[username] = count
        else:
            new_followers[username] += count
    elif command[0] == "Comment":
        comment = command[1]
        if username not in new_followers:
            new_followers[username] = 1
            followers += 1
        else:
            new_followers[username] += 1

    elif command[0] == "Blocked":
        if username in new_followers:
            new_followers.pop(username)
            followers -= 1
        else:
            print(f"{username} doesn't exist.")

print(f"{followers} followers")
for key, value in new_followers.items():
    print(f"{key}: {value}")
