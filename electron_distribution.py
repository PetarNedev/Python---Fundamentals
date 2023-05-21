number = int(input())
new_number = number
shell_list = []
for i in range(1, number + 1):
    result = 2 * i ** 2
    if new_number <= 0:
        break
    if result > new_number:
        shell_list.append(new_number)
        break
    new_number -= result
    shell_list.append(result)
print(shell_list)
