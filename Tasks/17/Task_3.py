import math


class Fraction:
    def __init__(self, numerator, denominator):
        """Ініціалізація дробу з чисельником та знаменником"""
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        # Спрощуємо дріб при створенні
        gcd = math.gcd(abs(numerator), abs(denominator))

        # Зберігаємо знак у чисельнику
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __add__(self, other):
        """Додавання дробів"""
        if isinstance(other, Fraction):
            new_num = self.numerator * other.denominator + other.numerator * self.denominator
            new_den = self.denominator * other.denominator
            return Fraction(new_num, new_den)
        elif isinstance(other, int):
            return Fraction(self.numerator + other * self.denominator, self.denominator)
        else:
            return NotImplemented

    def __sub__(self, other):
        """Віднімання дробів"""
        if isinstance(other, Fraction):
            new_num = self.numerator * other.denominator - other.numerator * self.denominator
            new_den = self.denominator * other.denominator
            return Fraction(new_num, new_den)
        elif isinstance(other, int):
            return Fraction(self.numerator - other * self.denominator, self.denominator)
        else:
            return NotImplemented

    def __mul__(self, other):
        """Множення дробів"""
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator,
                            self.denominator * other.denominator)
        elif isinstance(other, int):
            return Fraction(self.numerator * other, self.denominator)
        else:
            return NotImplemented

    def __truediv__(self, other):
        """Ділення дробів"""
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Fraction(self.numerator * other.denominator,
                            self.denominator * other.numerator)
        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Fraction(self.numerator, self.denominator * other)
        else:
            return NotImplemented

    def __eq__(self, other):
        """Порівняння на рівність"""
        if isinstance(other, Fraction):
            return (self.numerator == other.numerator and
                    self.denominator == other.denominator)
        elif isinstance(other, int):
            return self.numerator == other * self.denominator
        return False

    def __lt__(self, other):
        """Менше ніж"""
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < other.numerator * self.denominator
        elif isinstance(other, int):
            return self.numerator < other * self.denominator
        return NotImplemented

    def __le__(self, other):
        """Менше або дорівнює"""
        return self == other or self < other

    def __gt__(self, other):
        """Більше ніж"""
        if isinstance(other, Fraction):
            return self.numerator * other.denominator > other.numerator * self.denominator
        elif isinstance(other, int):
            return self.numerator > other * self.denominator
        return NotImplemented

    def __ge__(self, other):
        """Більше або дорівнює"""
        return self == other or self > other

    def __str__(self):
        """Строкове представлення для print()"""
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        """Офіційне представлення"""
        return f"Fraction({self.numerator}, {self.denominator})"


if __name__ == "__main__":
    # Тестування з прикладу
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(f"{x} + {y} = {x + y}")
    print(f"{x} + {y} == Fraction(3, 4): {x + y == Fraction(3, 4)}")

    # Додаткові тести
    print(f"\n{x} - {y} = {x - y}")
    print(f"{x} * {y} = {x * y}")
    print(f"{x} / {y} = {x / y}")

    print(f"\n{x} > {y}: {x > y}")
    print(f"{x} < {y}: {x < y}")
    print(f"{x} == Fraction(2, 4): {x == Fraction(2, 4)}")

    # Тест з цілими числами
    z = Fraction(3, 2)
    print(f"\n{z} + 2 = {z + 2}")
    print(f"{z} * 3 = {z * 3}")