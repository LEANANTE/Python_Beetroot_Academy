"""
Домашнє завдання: HashTable з __contains__ та __len__
Алгоритми пошуку та хешування

Реалізація хеш-таблиці з методом ланцюжків для вирішення колізій.
"""


class HashTable:
    """
    Хеш-таблиця з підтримкою операторів 'in' та функції len().
    
    Використовує метод ланцюжків (chaining) для вирішення колізій.
    Кожна комірка таблиці містить список пар (ключ, значення).
    """
    
    def __init__(self, size=10):
        """
        Ініціалізація хеш-таблиці.
        
        Args:
            size: розмір таблиці (кількість бакетів)
        """
        self.size = size
        self.table = [[] for _ in range(size)]
        self._count = 0  # Лічильник елементів
    
    def _hash(self, key):
        """
        Обчислює хеш-індекс для ключа.
        
        Args:
            key: ключ для хешування
            
        Returns:
            індекс у таблиці (0 до size-1)
        """
        return hash(key) % self.size
    
    def insert(self, key, value):
        """
        Вставляє або оновлює пару ключ-значення.
        
        Args:
            key: ключ
            value: значення
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        # Перевіряємо чи ключ вже існує
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Оновлюємо значення
                return
        
        # Додаємо новий елемент
        bucket.append((key, value))
        self._count += 1
    
    def get(self, key, default=None):
        """
        Повертає значення за ключем.
        
        Args:
            key: ключ для пошуку
            default: значення за замовчуванням
            
        Returns:
            значення або default якщо ключ не знайдено
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return default
    
    def delete(self, key):
        """
        Видаляє елемент за ключем.
        
        Args:
            key: ключ для видалення
            
        Raises:
            KeyError: якщо ключ не знайдено
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._count -= 1
                return
        
        raise KeyError(f"Ключ '{key}' не знайдено")
    
    # ==================== ОСНОВНІ МЕТОДИ ====================
    
    def __contains__(self, key):
        """
        Перевіряє наявність ключа в таблиці.
        Дозволяє використовувати оператор 'in'.
        
        Приклад використання:
            if 'name' in hash_table:
                print("Ключ існує!")
        
        Args:
            key: ключ для перевірки
            
        Returns:
            True якщо ключ існує, False інакше
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return True
        
        return False
    
    def __len__(self):
        """
        Повертає кількість елементів у таблиці.
        Дозволяє використовувати функцію len().
        
        Приклад використання:
            print(len(hash_table))  # Виведе кількість елементів
        
        Returns:
            кількість пар ключ-значення в таблиці
        """
        return self._count
    
    # ==================== ДОДАТКОВІ МЕТОДИ ====================
    
    def __getitem__(self, key):
        """
        Дозволяє доступ через квадратні дужки: hash_table[key]
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(f"Ключ '{key}' не знайдено")
    
    def __setitem__(self, key, value):
        """
        Дозволяє присвоєння через квадратні дужки: hash_table[key] = value
        """
        self.insert(key, value)
    
    def __delitem__(self, key):
        """
        Дозволяє видалення через del: del hash_table[key]
        """
        self.delete(key)
    
    def __repr__(self):
        """
        Повертає рядкове представлення таблиці.
        """
        items = []
        for bucket in self.table:
            for key, value in bucket:
                items.append(f"{key!r}: {value!r}")
        return "HashTable({" + ", ".join(items) + "})"
    
    def __str__(self):
        """
        Повертає читабельне представлення таблиці.
        """
        items = []
        for bucket in self.table:
            for key, value in bucket:
                items.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(items) + "}"
    
    def keys(self):
        """Повертає всі ключі."""
        result = []
        for bucket in self.table:
            for key, value in bucket:
                result.append(key)
        return result
    
    def values(self):
        """Повертає всі значення."""
        result = []
        for bucket in self.table:
            for key, value in bucket:
                result.append(value)
        return result
    
    def items(self):
        """Повертає всі пари (ключ, значення)."""
        result = []
        for bucket in self.table:
            for key, value in bucket:
                result.append((key, value))
        return result


# ===================== ТЕСТУВАННЯ =====================
if __name__ == "__main__":
    print("=" * 60)
    print("HASH TABLE з __contains__ та __len__")
    print("=" * 60)
    
    # Створення хеш-таблиці
    ht = HashTable()
    
    # Вставка елементів
    print("\n--- Вставка елементів ---")
    ht.insert("name", "Олексій")
    ht.insert("age", 25)
    ht.insert("city", "Київ")
    ht.insert("language", "Python")
    ht.insert("level", "Junior")
    
    print(f"Хеш-таблиця: {ht}")
    
    # ========== ТЕСТ __len__ ==========
    print("\n--- Тест __len__ ---")
    print(f"len(ht) = {len(ht)}")  # Очікується: 5
    
    # ========== ТЕСТ __contains__ ==========
    print("\n--- Тест __contains__ (оператор 'in') ---")
    
    # Перевірка існуючих ключів
    print(f"'name' in ht:     {('name' in ht)}")      # True
    print(f"'age' in ht:      {('age' in ht)}")       # True
    print(f"'city' in ht:     {('city' in ht)}")      # True
    
    # Перевірка неіснуючих ключів
    print(f"'country' in ht:  {('country' in ht)}")   # False
    print(f"'salary' in ht:   {('salary' in ht)}")    # False
    
    # Важливо: 'in' перевіряє КЛЮЧІ, а не значення!
    print(f"'Олексій' in ht:  {('Олексій' in ht)}")   # False (це значення!)
    print(f"'Python' in ht:   {('Python' in ht)}")    # False (це значення!)
    
    # ========== ТЕСТ видалення ==========
    print("\n--- Тест видалення ---")
    print(f"До видалення: len(ht) = {len(ht)}")
    print(f"'age' in ht: {('age' in ht)}")
    
    ht.delete("age")
    
    print(f"\nПісля видалення 'age':")
    print(f"len(ht) = {len(ht)}")
    print(f"'age' in ht: {('age' in ht)}")
    
    # ========== ТЕСТ додаткових методів ==========
    print("\n--- Додаткові методи ---")
    
    # Доступ через []
    print(f"ht['name'] = {ht['name']}")
    
    # Присвоєння через []
    ht['email'] = 'test@example.com'
    print(f"Після ht['email'] = 'test@example.com': len(ht) = {len(ht)}")
    
    # Всі ключі та значення
    print(f"\nКлючі: {ht.keys()}")
    print(f"Значення: {ht.values()}")
    
    # ========== ФІНАЛЬНИЙ СТАН ==========
    print("\n" + "=" * 60)
    print("ФІНАЛЬНИЙ СТАН")
    print("=" * 60)
    print(f"Хеш-таблиця: {ht}")
    print(f"Кількість елементів: {len(ht)}")
    print(f"Ключі в таблиці: {ht.keys()}")
