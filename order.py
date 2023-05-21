def orders(product, quality):
    result = 0
    if product == "coffee":
        result = quality * 1.50
    elif product == "coke":
        result = quality * 1.40
    elif product == "water":
        result = quality * 1
    elif product == "snacks":
        result = quality * 2
    return result


product_order = input()
quality_order = int(input())

print(f"{orders(product_order, quality_order):.2f}")
