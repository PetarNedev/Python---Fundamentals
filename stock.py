products = input().split()
bakery = {}

for index in range(0, len(products), 2):
    key = products[index]
    value = int(products[index + 1])
    bakery[key] = value

searched_products = input().split()

for word in searched_products:
    if word in bakery:
        print(f"We have {bakery.get(word)} of {word} left")
    else:
        print(f"Sorry, we don't have {word}")
