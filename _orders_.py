order_price = {}
order_quality = {}

while True:
    line = input().split()
    if line == ["buy"]:
        break
    name = line[0]
    price = float(line[1])
    quantity = int(line[2])

    if name not in order_price and name not in order_quality:
        order_quality[name] = quantity
        order_price[name] = price
    else:
        order_quality[name] += quantity
        order_price[name] = price

for product in order_quality:
    price = order_price[product]
    quantity = order_quality[product]
    total_price = price * quantity
    print(f"{product} -> {total_price:.2f}")
