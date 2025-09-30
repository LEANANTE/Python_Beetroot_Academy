# Valid Phone Number Program
# Перевірка чи номер телефону валідний

def check_phone_number(phone):
    """
    Перевіряє чи номер телефону валідний:
    - Тільки цифри,
    - Довжина рівно 10 символів
    """
    print(f"\nChecking phone number: {phone}")

    # Перевіряємо обидві умови
    if len(phone) == 10 and phone.isdigit():
        print("✓ Valid phone number!")
        return True
    else:
        print("✗ Invalid phone number!")
        # Пояснюємо причину
        if len(phone) != 10:
            print(f"  Reason: Length is {len(phone)}, expected 10")
        if not phone.isdigit():
            print("  Reason: Contains non-numeric characters")
        return False


# Тестування
print("TASK 2: Valid Phone Number")
print("-" * 40)

# Test 1 - Valid
check_phone_number("1234567890")

# Test 2 - Too short
check_phone_number("123456789")

# Test 3 - Too long
check_phone_number("12345678901")

# Test 4 - Contains letters
check_phone_number("12345abcde")

# Test 5 - Contains special characters
check_phone_number("123-456-789")