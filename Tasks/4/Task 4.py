#Name Check Program
# Перевірка імені незалежно від регістру

print("TASK 4: Name Check")
print("-" * 40)

# Збережене ім'я (в нижньому регістрі)
stored_name = "heorhii"

print(f"Stored name: '{stored_name}'")
print("Please enter your name to verify:")

# Отримуємо ім'я від користувача
input_name = input("Your name: ")

# Порівнюємо імена, ігноруючи регістр
if input_name.lower() == stored_name:
    print("True - Names match! Access granted.")
else:
    print("False - Names don't match! Access denied.")

# Додаткова інформація для демонстрації
print("\n" + "-" * 40)
print("How it works:")
print(f"Input: '{input_name}'")
print(f"Input lowercased: '{input_name.lower()}'")
print(f"Stored name: '{stored_name}'")
print(f"Match: {input_name.lower() == stored_name}")

# Приклади:
print("\n" + "-" * 40)
print("Test examples:")

test_names = ["Heorhii", "HEORHII", "heorhii", "HeoRhii", "Anton"]

for name in test_names:
    result = name.lower() == stored_name
    print(f"'{name}' → {result}")