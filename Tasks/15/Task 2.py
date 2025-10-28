class Dog:
    age_factor = 7  # Class variable

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * Dog.age_factor


# Тестування
my_dog = Dog(5)
print(f"Dog's age in human years: {my_dog.human_age()}")  # 35