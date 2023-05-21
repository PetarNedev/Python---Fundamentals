product_dict = {}

while True:
    product = input().split(": ")
    if product == ["statistics"]:
        break
    key = product[0]
    value = int(product[1])
    if key in product_dict:
        value += product_dict[key]
    product_dict[key] = value

print("Products in stock:")
for el in product_dict:
    print(f"- {el}: {product_dict.get(el)}")
print(f"Total Products: {len(product_dict)}")
print(f"Total Quantity: {sum(product_dict.values())}")
