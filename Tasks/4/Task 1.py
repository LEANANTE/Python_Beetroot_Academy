# String Manipulation
# Отримати рядок з перших 2 і останніх 2 символів

def get_first_last_chars(string):
    """
    Повертає рядок з перших 2 і останніх 2 символів,
    Якщо довжина < 2, повертає порожній рядок.
    """
    # Перевіряємо довжину рядка
    if len(string) < 2:
        return ""
    else:
        # Перші 2 символи: string[0:2] або string[:2]
        # Останні 2 символи: string[-2:]
        result = string[0:2] + string[-2:]
        return result


# Тестування
print("TASK 1: String Manipulation")
print("-" * 40)

# Test 1
test_string1 = 'helloworld'
print(f"Input: '{test_string1}'")
print(f"Output: '{get_first_last_chars(test_string1)}'")
print(f"Expected: 'held'\n")

# Test 2
test_string2 = 'my'
print(f"Input: '{test_string2}'")
print(f"Output: '{get_first_last_chars(test_string2)}'")
print(f"Expected: 'mymy'\n")

# Test 3
test_string3 = 'x'
print(f"Input: '{test_string3}'")
print(f"Output: '{get_first_last_chars(test_string3)}'")
print(f"Expected: Empty String")