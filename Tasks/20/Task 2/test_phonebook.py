import unittest
import json
import os
import tempfile
from unittest.mock import patch, MagicMock
from phonebook import PhoneBook

# запуск через команду python -m unittest test_phonebook.py -v

class TestPhoneBook(unittest.TestCase):

    def setUp(self):
        """Створюємо тимчасовий файл для тестів"""
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.phonebook = PhoneBook(self.temp_file.name)

    def tearDown(self):
        """Видаляємо тимчасовий файл після тестів"""
        try:
            os.unlink(self.temp_file.name)
        except:
            pass

    # ========== Тести завантаження/збереження ==========

    def test_init_creates_empty_phonebook(self):
        """Тест створення порожньої телефонної книги"""
        self.assertEqual(self.phonebook.contacts, [])
        self.assertEqual(self.phonebook.filename, self.temp_file.name)

    def test_load_existing_data(self):
        """Тест завантаження існуючих даних"""
        test_data = [
            {"first_name": "Тарас", "last_name": "Шевченко",
             "phone": "123456", "city": "Київ", "state": "Київська"}
        ]

        # Записуємо тестові дані
        with open(self.temp_file.name, 'w', encoding='utf-8') as f:
            json.dump(test_data, f)

        # Створюємо новий екземпляр і перевіряємо завантаження
        pb = PhoneBook(self.temp_file.name)
        self.assertEqual(len(pb.contacts), 1)
        self.assertEqual(pb.contacts[0]["first_name"], "Тарас")

    def test_save_data(self):
        """Тест збереження даних"""
        self.phonebook.contacts = [
            {"first_name": "Іван", "last_name": "Франко",
             "phone": "987654", "city": "Львів", "state": "Львівська"}
        ]
        self.phonebook.save_data()

        # Читаємо файл і перевіряємо
        with open(self.temp_file.name, 'r', encoding='utf-8') as f:
            saved_data = json.load(f)

        self.assertEqual(len(saved_data), 1)
        self.assertEqual(saved_data[0]["first_name"], "Іван")

    def test_load_corrupted_file(self):
        """Тест завантаження пошкодженого файлу"""
        # Записуємо некоректний JSON
        with open(self.temp_file.name, 'w') as f:
            f.write("not a json{]")

        pb = PhoneBook(self.temp_file.name)
        self.assertEqual(pb.contacts, [])  # Має створити порожню книгу

    # ========== Тести додавання контактів ==========

    @patch('builtins.input')
    def test_add_entry_success(self, mock_input):
        """Тест успішного додавання контакту"""
        mock_input.side_effect = ["Петро", "Петренко", "380501234567", "Полтава", "Полтавська"]

        self.phonebook.add_entry()

        self.assertEqual(len(self.phonebook.contacts), 1)
        contact = self.phonebook.contacts[0]
        self.assertEqual(contact["first_name"], "Петро")
        self.assertEqual(contact["phone"], "380501234567")

    @patch('builtins.input')
    def test_add_entry_empty_phone(self, mock_input):
        """Тест додавання контакту без телефону"""
        mock_input.side_effect = ["Петро", "Петренко", "", "Полтава", "Полтавська"]

        self.phonebook.add_entry()

        self.assertEqual(len(self.phonebook.contacts), 0)  # Не має додати

    @patch('builtins.input')
    def test_add_duplicate_phone(self, mock_input):
        """Тест додавання дублікату телефону"""
        # Додаємо перший контакт
        self.phonebook.contacts = [
            {"first_name": "Іван", "last_name": "Іваненко",
             "phone": "123456", "city": "Київ", "state": "Київська"}
        ]

        # Намагаємось додати з тим самим номером
        mock_input.side_effect = ["Петро", "Петренко", "123456", "Львів", "Львівська"]

        self.phonebook.add_entry()

        self.assertEqual(len(self.phonebook.contacts), 1)  # Не має додати дублікат

    # ========== Тести пошуку ==========

    def test_search_by_first_name(self):
        """Тест пошуку за ім'ям"""
        self.phonebook.contacts = [
            {"first_name": "Петро", "last_name": "Петренко",
             "phone": "111", "city": "Київ", "state": "Київська"},
            {"first_name": "Павло", "last_name": "Павленко",
             "phone": "222", "city": "Львів", "state": "Львівська"},
            {"first_name": "Петро", "last_name": "Іваненко",
             "phone": "333", "city": "Одеса", "state": "Одеська"}
        ]

        with patch('builtins.input', return_value='Петро'):
            with patch.object(self.phonebook, '_display_results') as mock_display:
                self.phonebook.search_by_first_name()

                # Перевіряємо що знайшло 2 Петра
                results = mock_display.call_args[0][0]
                self.assertEqual(len(results), 2)
                self.assertTrue(all(c["first_name"] == "Петро" for c in results))

    def test_search_by_phone_partial(self):
        """Тест пошуку за частиною номера"""
        self.phonebook.contacts = [
            {"first_name": "Іван", "last_name": "Іваненко",
             "phone": "380501234567", "city": "Київ", "state": "Київська"},
            {"first_name": "Петро", "last_name": "Петренко",
             "phone": "380507654321", "city": "Львів", "state": "Львівська"}
        ]

        with patch('builtins.input', return_value='050'):
            with patch.object(self.phonebook, '_display_results') as mock_display:
                self.phonebook.search_by_phone()

                results = mock_display.call_args[0][0]
                self.assertEqual(len(results), 2)  # Обидва містять "050"

    def test_search_by_full_name(self):
        """Тест пошуку за повним ім'ям"""
        self.phonebook.contacts = [
            {"first_name": "Іван", "last_name": "Франко",
             "phone": "111", "city": "Львів", "state": "Львівська"},
            {"first_name": "Іван", "last_name": "Котляревський",
             "phone": "222", "city": "Полтава", "state": "Полтавська"}
        ]

        with patch('builtins.input', return_value='Іван Франко'):
            with patch.object(self.phonebook, '_display_results') as mock_display:
                self.phonebook.search_by_full_name()

                results = mock_display.call_args[0][0]
                self.assertEqual(len(results), 1)
                self.assertEqual(results[0]["last_name"], "Франко")

    def test_search_by_city_state(self):
        """Тест пошуку за містом або областю"""
        self.phonebook.contacts = [
            {"first_name": "Іван", "last_name": "Іваненко",
             "phone": "111", "city": "Київ", "state": "Київська"},
            {"first_name": "Петро", "last_name": "Петренко",
             "phone": "222", "city": "Бориспіль", "state": "Київська"}
        ]

        with patch('builtins.input', return_value='Київська'):
            with patch.object(self.phonebook, '_display_results') as mock_display:
                self.phonebook.search_by_city_state()

                results = mock_display.call_args[0][0]
                self.assertEqual(len(results), 2)  # Обидва з Київської області

    # ========== Тести видалення ==========

    @patch('builtins.input')
    def test_delete_record_confirmed(self, mock_input):
        """Тест видалення контакту з підтвердженням"""
        self.phonebook.contacts = [
            {"first_name": "Іван", "last_name": "Іваненко",
             "phone": "123456", "city": "Київ", "state": "Київська"}
        ]

        mock_input.side_effect = ["123456", "так"]

        self.phonebook.delete_record()

        self.assertEqual(len(self.phonebook.contacts), 0)

    @patch('builtins.input')
    def test_delete_record_cancelled(self, mock_input):
        """Тест скасування видалення"""
        self.phonebook.contacts = [
            {"first_name": "Іван", "last_name": "Іваненко",
             "phone": "123456", "city": "Київ", "state": "Київська"}
        ]

        mock_input.side_effect = ["123456", "ні"]

        self.phonebook.delete_record()

        self.assertEqual(len(self.phonebook.contacts), 1)  # Не видалено

    @patch('builtins.input')
    def test_delete_nonexistent_record(self, mock_input):
        """Тест видалення неіснуючого контакту"""
        mock_input.return_value = "999999"

        self.phonebook.delete_record()

        # Нічого не має статися, контакти залишаються порожніми
        self.assertEqual(len(self.phonebook.contacts), 0)

    # ========== Тести оновлення ==========

    @patch('builtins.input')
    def test_update_record_partial(self, mock_input):
        """Тест часткового оновлення контакту"""
        self.phonebook.contacts = [
            {"first_name": "Іван", "last_name": "Іваненко",
             "phone": "123456", "city": "Київ", "state": "Київська"}
        ]

        # Оновлюємо тільки місто
        mock_input.side_effect = ["123456", "", "", "", "Львів", ""]

        self.phonebook.update_record()

        contact = self.phonebook.contacts[0]
        self.assertEqual(contact["first_name"], "Іван")  # Не змінено
        self.assertEqual(contact["city"], "Львів")  # Змінено
        self.assertEqual(contact["state"], "Київська")  # Не змінено

    @patch('builtins.input')
    def test_update_duplicate_phone(self, mock_input):
        """Тест оновлення на дублікат номера"""
        self.phonebook.contacts = [
            {"first_name": "Іван", "last_name": "Іваненко",
             "phone": "111", "city": "Київ", "state": "Київська"},
            {"first_name": "Петро", "last_name": "Петренко",
             "phone": "222", "city": "Львів", "state": "Львівська"}
        ]

        # Намагаємось змінити номер першого на номер другого
        mock_input.side_effect = ["111", "", "", "222", "", ""]

        self.phonebook.update_record()

        # Номер не має змінитися
        self.assertEqual(self.phonebook.contacts[0]["phone"], "111")

    # ========== Тести відображення ==========

    def test_show_all_contacts_empty(self):
        """Тест відображення порожньої книги"""
        with patch('builtins.print') as mock_print:
            self.phonebook.show_all_contacts()

            # Перевіряємо що виводить повідомлення про порожню книгу
            calls = [str(call) for call in mock_print.call_args_list]
            self.assertTrue(any("порожня" in str(call).lower() for call in calls))

    def test_show_all_contacts_with_data(self):
        """Тест відображення контактів"""
        self.phonebook.contacts = [
            {"first_name": "Іван", "last_name": "Іваненко",
             "phone": "111", "city": "Київ", "state": "Київська"},
            {"first_name": "Петро", "last_name": "Петренко",
             "phone": "222", "city": "Львів", "state": "Львівська"}
        ]

        with patch.object(self.phonebook, '_display_contact') as mock_display:
            self.phonebook.show_all_contacts()

            # Перевіряємо що викликано для кожного контакту
            self.assertEqual(mock_display.call_count, 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)