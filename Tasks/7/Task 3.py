# List comprehension для створення списку кортежів (i, j) де j = i²
print("=" * 50)
print("TASK 3 - List comprehension")
print("=" * 50)

# Створюємо список кортежів (i, i²) для i від 1 до 10
squares_list = [(i, i**2) for i in range(1, 11)]

print("Список кортежів (i, i²) для i від 1 до 10:")
for item in squares_list:
    print(f"  {item[0]:2} -> {item[1]:3}")
print()