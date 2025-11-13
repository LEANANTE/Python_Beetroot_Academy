from typing import List, Tuple

# We assume that all lists passed to functions are the same length N

Match
big
O
complexities
with the code snippets below

# answers
# 1 - log n
# 2 - n^2
# 3 - n
# 4 - n^2
# 5 - 1
# 6 - n


def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res


def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n


def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)
    return temp


def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res


def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res


def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n

# Відповіді:
# question1 → O(n²)
# Зовнішній цикл: O(n) по first_list
# Операція in second_list всередині циклу: O(n)
# Загалом: O(n) × O(n) = O(n²)

# question2 → O(1)
# Цикл виконується фіксовану кількість разів (10)
# Не залежить від розміру вхідних даних
# Константна складність

# question3 → O(n²)
# Зовнішній цикл по second_list: O(n)
# Внутрішній цикл по temp: O(n)
# Вкладені цикли = O(n²)

# question4 → O(n)
# Один прохід по списку
# Лінійна складність

# question5 → O(n²)
# Два вкладені цикли від 0 до n
# Створює n × n пар
# Квадратична складність

# question6 → O(log n)
# На кожній ітерації n ділиться на 2
# Кількість ітерацій = log₂(n)
# Логарифмічна складність

# Підсумок відповідей:

# question1: n²
# question2: 1
# question3: n²
# question4: n
# question5: n²
# question6: log n

# У функції question3 є помилка в коді - замість temp.append(second_list) має бути temp.append(el_second_list), але це не впливає на складність алгоритму.