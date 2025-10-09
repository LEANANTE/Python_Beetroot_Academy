# Обчислення загальної вартості товарів на складі
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def calculate_total_prices(stock, prices):
    """
    Обчислює загальну вартість кожного товару на складі.
    Повертає словник з сумами цін за типами товарів.
    """
    total_prices = {}
    for item in stock:
        if item in prices:
            total_prices[item] = stock[item] * prices[item]
    return total_prices
print("=" * 50)
print("TASK 2 - загальна вартість товарів")
print("=" * 50)
result2 = calculate_total_prices(stock, prices)
print(f"Склад: {stock}")
print(f"Ціни: {prices}")
print(f"Загальні вартості: {result2}")
print(f"Загальна сума всіх товарів: {sum(result2.values())}")
print()
