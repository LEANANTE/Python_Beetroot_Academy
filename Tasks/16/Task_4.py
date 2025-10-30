class CustomException(Exception):
    def __init__(self, msg):
        # Викликаємо конструктор батьківського класу
        super().__init__(msg)

        # Логуємо повідомлення в файл
        try:
            with open('logs.txt', 'a') as f:
                from datetime import datetime
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{timestamp}] ERROR: {msg}\n")
        except IOError:
            print(f"Could not write to logs.txt: {msg}")


# Приклад використання:
try:
    raise CustomException("Something went wrong!")
except CustomException as e:
    print(f"Caught exception: {e}")