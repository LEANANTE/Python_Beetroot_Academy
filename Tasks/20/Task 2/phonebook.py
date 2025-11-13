#!/usr/bin/env python3
"""
Телефонна книга з підтримкою JSON
Використання: python phonebook.py phonebook_name.json
"""

import json
import sys
import os


class PhoneBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = []
        self.load_data()

    def load_data(self):
        """Завантаження даних з JSON файлу"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as file:
                    self.contacts = json.load(file)
                print(f"✓ Завантажено {len(self.contacts)} контактів з {self.filename}")
            except json.JSONDecodeError:
                print(f"⚠ Файл {self.filename} пошкоджено. Створюю нову телефонну книгу.")
                self.contacts = []
            except Exception as e:
                print(f"⚠ Помилка при завантаженні: {e}")
                self.contacts = []
        else:
            print(f"📝 Створюю нову телефонну книгу: {self.filename}")
            self.contacts = []

    def save_data(self):
        """Збереження даних у JSON файл"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(self.contacts, file, ensure_ascii=False, indent=2)
            print(f"✓ Дані збережено в {self.filename}")
        except Exception as e:
            print(f"❌ Помилка при збереженні: {e}")

    def add_entry(self):
        """Додавання нового контакту"""
        print("\n=== Додавання нового контакту ===")
        contact = {
            "first_name": input("Ім'я: ").strip(),
            "last_name": input("Прізвище: ").strip(),
            "phone": input("Телефон: ").strip(),
            "city": input("Місто: ").strip(),
            "state": input("Область/Штат: ").strip()
        }

        if not contact["phone"]:
            print("❌ Телефон є обов'язковим полем!")
            return

        # Перевірка на дублікати
        if any(c["phone"] == contact["phone"] for c in self.contacts):
            print(f"⚠ Контакт з номером {contact['phone']} вже існує!")
            return

        self.contacts.append(contact)
        print("✓ Контакт додано успішно!")

    def search_by_first_name(self):
        """Пошук за ім'ям"""
        name = input("\nВведіть ім'я для пошуку: ").strip().lower()
        results = [c for c in self.contacts if c["first_name"].lower().startswith(name)]
        self._display_results(results)

    def search_by_last_name(self):
        """Пошук за прізвищем"""
        name = input("\nВведіть прізвище для пошуку: ").strip().lower()
        results = [c for c in self.contacts if c["last_name"].lower().startswith(name)]
        self._display_results(results)

    def search_by_full_name(self):
        """Пошук за повним ім'ям"""
        full_name = input("\nВведіть повне ім'я (ім'я прізвище): ").strip().lower()
        results = []
        for c in self.contacts:
            contact_full_name = f"{c['first_name']} {c['last_name']}".lower()
            if full_name in contact_full_name:
                results.append(c)
        self._display_results(results)

    def search_by_phone(self):
        """Пошук за номером телефону"""
        phone = input("\nВведіть номер телефону (або його частину): ").strip()
        results = [c for c in self.contacts if phone in c["phone"]]
        self._display_results(results)

    def search_by_city_state(self):
        """Пошук за містом або областю"""
        location = input("\nВведіть місто або область: ").strip().lower()
        results = []
        for c in self.contacts:
            if (location in c["city"].lower() or
                    location in c["state"].lower()):
                results.append(c)
        self._display_results(results)

    def delete_record(self):
        """Видалення контакту за номером телефону"""
        phone = input("\nВведіть номер телефону для видалення: ").strip()

        for i, contact in enumerate(self.contacts):
            if contact["phone"] == phone:
                self._display_contact(contact)
                confirm = input("\nВидалити цей контакт? (так/ні): ").strip().lower()
                if confirm in ['так', 'yes', 'y', 'т']:
                    self.contacts.pop(i)
                    print("✓ Контакт видалено!")
                    return
                else:
                    print("Видалення скасовано.")
                    return

        print(f"❌ Контакт з номером {phone} не знайдено!")

    def update_record(self):
        """Оновлення контакту за номером телефону"""
        phone = input("\nВведіть номер телефону для оновлення: ").strip()

        for contact in self.contacts:
            if contact["phone"] == phone:
                print("\nПоточні дані:")
                self._display_contact(contact)

                print("\nВведіть нові дані (натисніть Enter, щоб залишити без змін):")

                new_first_name = input(f"Ім'я [{contact['first_name']}]: ").strip()
                new_last_name = input(f"Прізвище [{contact['last_name']}]: ").strip()
                new_phone = input(f"Телефон [{contact['phone']}]: ").strip()
                new_city = input(f"Місто [{contact['city']}]: ").strip()
                new_state = input(f"Область/Штат [{contact['state']}]: ").strip()

                # Оновлюємо тільки непорожні поля
                if new_first_name:
                    contact["first_name"] = new_first_name
                if new_last_name:
                    contact["last_name"] = new_last_name
                if new_phone:
                    # Перевірка на дублікат номера
                    if any(c["phone"] == new_phone and c != contact for c in self.contacts):
                        print(f"⚠ Номер {new_phone} вже використовується!")
                        return
                    contact["phone"] = new_phone
                if new_city:
                    contact["city"] = new_city
                if new_state:
                    contact["state"] = new_state

                print("✓ Контакт оновлено!")
                return

        print(f"❌ Контакт з номером {phone} не знайдено!")

    def show_all_contacts(self):
        """Показати всі контакти"""
        if not self.contacts:
            print("\n📭 Телефонна книга порожня")
            return

        print(f"\n=== Всі контакти ({len(self.contacts)}) ===")
        for i, contact in enumerate(self.contacts, 1):
            print(f"\n{i}.")
            self._display_contact(contact)

    def _display_contact(self, contact):
        """Відображення одного контакту"""
        print(f"  Ім'я: {contact['first_name']} {contact['last_name']}")
        print(f"  Телефон: {contact['phone']}")
        print(f"  Місто: {contact['city']}")
        print(f"  Область/Штат: {contact['state']}")

    def _display_results(self, results):
        """Відображення результатів пошуку"""
        if not results:
            print("\n❌ Нічого не знайдено")
            return

        print(f"\n=== Знайдено контактів: {len(results)} ===")
        for i, contact in enumerate(results, 1):
            print(f"\n{i}.")
            self._display_contact(contact)

    def run(self):
        """Головний цикл програми"""
        while True:
            print("\n" + "=" * 50)
            print("📞 ТЕЛЕФОННА КНИГА")
            print("=" * 50)
            print("1. Додати новий контакт")
            print("2. Пошук за ім'ям")
            print("3. Пошук за прізвищем")
            print("4. Пошук за повним ім'ям")
            print("5. Пошук за номером телефону")
            print("6. Пошук за містом або областю")
            print("7. Видалити контакт")
            print("8. Оновити контакт")
            print("9. Показати всі контакти")
            print("0. Вийти та зберегти")

            choice = input("\nОберіть опцію: ").strip()

            if choice == "1":
                self.add_entry()
            elif choice == "2":
                self.search_by_first_name()
            elif choice == "3":
                self.search_by_last_name()
            elif choice == "4":
                self.search_by_full_name()
            elif choice == "5":
                self.search_by_phone()
            elif choice == "6":
                self.search_by_city_state()
            elif choice == "7":
                self.delete_record()
            elif choice == "8":
                self.update_record()
            elif choice == "9":
                self.show_all_contacts()
            elif choice == "0":
                self.save_data()
                print("\nДо побачення! 👋")
                break
            else:
                print("⚠ Невірна опція! Спробуйте ще раз.")


def main():
    # Перевірка аргументів командного рядка
    if len(sys.argv) != 2:
        print("❌ Помилка: Вкажіть назву файлу телефонної книги!")
        print("Використання: python phonebook.py <назва_файлу.json>")
        print("Приклад: python phonebook.py my_contacts.json")
        sys.exit(1)

    filename = sys.argv[1]

    # Перевірка розширення файлу
    if not filename.endswith('.json'):
        filename += '.json'

    # Створення та запуск телефонної книги
    phonebook = PhoneBook(filename)
    phonebook.run()


if __name__ == "__main__":
    main()