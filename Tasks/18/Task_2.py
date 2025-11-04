class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []  # Приватний атрибут

    @property
    def workers(self):
        """Getter для списку працівників"""
        return self._workers.copy()  # Повертаємо копію для захисту

    def add_worker(self, worker):
        """Метод для додавання працівників"""
        if not isinstance(worker, Worker):
            raise TypeError("Can only add Worker instances")
        if worker not in self._workers:
            self._workers.append(worker)
            # Встановлюємо себе як боса для працівника
            worker._boss = self


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        # Використовуємо setter для валідації
        self.boss = boss

    @property
    def boss(self):
        """Getter для боса"""
        return self._boss

    @boss.setter
    def boss(self, value):
        """Setter з перевіркою типу"""
        if not isinstance(value, Boss):
            raise TypeError("Boss must be an instance of Boss class")

        # Видаляємо з попереднього боса, якщо був
        if self._boss and self in self._boss._workers:
            self._boss._workers.remove(self)

        # Встановлюємо нового боса
        self._boss = value
        # Додаємо себе до списку працівників нового боса
        if self not in value._workers:
            value._workers.append(self)


# Тестування
boss1 = Boss(1, "Alice", "TechCorp")
boss2 = Boss(2, "Bob", "TechCorp")

worker1 = Worker(101, "John", "TechCorp", boss1)
worker2 = Worker(102, "Jane", "TechCorp", boss1)

print(f"Boss {boss1.name} has {len(boss1.workers)} workers")

# Зміна боса
worker1.boss = boss2
print(f"Worker {worker1.name} now works for {worker1.boss.name}")
print(f"Boss {boss1.name} has {len(boss1.workers)} workers")
print(f"Boss {boss2.name} has {len(boss2.workers)} workers")