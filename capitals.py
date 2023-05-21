country = input().split(", ")
capital = input().split(", ")

resources = dict(zip(country, capital))
for el in resources:
    print(f"{el} -> {resources[el]}")
