# Робота з днями тижня
print("=" * 50)
print("TASK 4 - Словники з днями тижня")
print("=" * 50)

# 1. Створити список із днями тижня
days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("1. Список днів тижня:")
print(f"   {days_list}")
print()

# 2. Створити словник {1: "Monday", 2: "Tuesday", ...}
# виводимо в один рядок з dict comprehension
days_dict = {i+1: day for i, day in enumerate(days_list)}
print("2. Словник (номер -> день):")
print(f"   {days_dict}")
print()

# 3. Створити зворотний словник {"Monday": 1, "Tuesday": 2, ...}
# в один рядок з dict comprehension
reverse_days_dict = {day: i+1 for i, day in enumerate(days_list)}
print("3. Зворотний словник (день -> номер):")
print(f"   {reverse_days_dict}")
print()