import re


class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.validate(email)

    @classmethod
    def validate(cls, email: str):
        """Validates if the email has a valid format"""
        # Regex pattern for email validation
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not isinstance(email, str):
            raise TypeError("Email must be a string")

        if not re.match(email_pattern, email):
            raise ValueError(f"Invalid email format: {email}")

        return True


# Тестування
try:
    user1 = User("John", "john@example.com")  # Валідний
    print(f"User created: {user1.username}")

    user2 = User("Jane", "invalid.email")  # Невалідний - викине помилку
except ValueError as e:
    print(f"Error: {e}")