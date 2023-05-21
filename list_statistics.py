number_of_lines = int(input())
positive = []
negative = []

for i in range(number_of_lines):
    numbers = int(input())
    if numbers >= 0:
        positive.append(numbers)
    else:
        negative.append(numbers)
print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")
