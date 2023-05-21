from math import ceil
numbers_as_str = [int(x) for x in input().split(", ")]
low_boundary = 1
high_boundary = 10
group_count = ceil(max(numbers_as_str) / 10)
for idx in range(1, group_count + 1):
    grouped_num = [x for x in numbers_as_str if low_boundary <= x <= high_boundary]
    print(f"Group of {10 * idx}'s: {grouped_num}")
    low_boundary += 10
    high_boundary += 10

