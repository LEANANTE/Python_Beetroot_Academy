# імпорт функції з module1
from module1 import greet, calculate_area

def enhanced_greeting(name, age):
    """Використовує greet з module1 та додає більше інформації"""
    basic_greeting = greet(name)
    return f"{basic_greeting}\nТобі {age} років."

def circle_info(radius):
    """Надає повну інформацію про коло, використовуючи module1"""
    area = calculate_area(radius)
    circumference = 2 * 3.14159 * radius
    return {
        'радіус': radius,
        'площа': area,
        'довжина_кола': circumference
    }