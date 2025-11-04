class Animal:
    """Базовий клас для тварин"""

    def talk(self):
        raise NotImplementedError("Subclass must implement talk method")


class Dog(Animal):
    """Клас собаки, що наслідує Animal"""

    def talk(self):
        print("woof woof")


class Cat(Animal):
    """Клас кота, що наслідує Animal"""

    def talk(self):
        print("meow")


def make_animal_talk(animal):
    """Генерична функція, що приймає екземпляр Dog або Cat"""
    animal.talk()


# Тестування
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    print("Dog says:")
    make_animal_talk(dog)  # Виведе: woof woof

    print("Cat says:")
    make_animal_talk(cat)  # Виведе: meow