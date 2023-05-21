first_list = input().split(", ")
second_list = input().split(", ")

result = []

for i in first_list:
    for j in second_list:
        found_substring = i in j
        if found_substring:
            result.append(i)
            break

print(result)

