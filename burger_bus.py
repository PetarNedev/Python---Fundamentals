number_of_city = int(input())

visited_city = 0
total_profit = 0

for city in range(number_of_city):
    name_of_city = input()
    income = float(input())
    expenses = float(input())

    visited_city += 1
    profit = 0

    if visited_city % 3 == 0:
        profit = income - (expenses * 1.5)

    elif visited_city % 5 == 0:
        profit = (income * 0.9) - expenses
    else:
        profit = income - expenses
    total_profit += profit

    print(f"In {name_of_city} Burger Bus earned {profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")
