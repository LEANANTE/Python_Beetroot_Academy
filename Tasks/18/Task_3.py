from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(func):
        """Декоратор для конвертації результату в int"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except (ValueError, TypeError):
                return result

        return wrapper

    @staticmethod
    def to_str(func):
        """Декоратор для конвертації результату в str"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)

        return wrapper

    @staticmethod
    def to_bool(func):
        """Декоратор для конвертації результату в bool"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            # Спеціальна логіка для рядків
            if isinstance(result, str):
                if result.lower() in ('true', '1', 'yes'):
                    return True
                elif result.lower() in ('false', '0', 'no', ''):
                    return False
            return bool(result)

        return wrapper

    @staticmethod
    def to_float(func):
        """Декоратор для конвертації результату в float"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except (ValueError, TypeError):
                return result

        return wrapper


# Тестування
@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


@TypeDecorators.to_float
def get_number(string: str):
    return string


@TypeDecorators.to_str
def get_value(number: int):
    return number


# Перевірка
assert do_nothing('25') == 25
assert do_something('True') is True
assert get_number('3.14') == 3.14
assert get_value(42) == '42'

print("All tests passed!")