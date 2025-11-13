import pytest
import tempfile
import os
from pathlib import Path
from unittest.mock import patch, MagicMock
from file_context_manager import FileContextManager


class TestFileContextManager:

    @pytest.fixture(autouse=True)
    def reset_statistics(self):
        """Скидаємо статистику перед кожним тестом"""
        FileContextManager.reset_statistics()
        yield
        FileContextManager.reset_statistics()

    @pytest.fixture
    def temp_file(self):
        """Створюємо тимчасовий файл для тестів"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("Test content\nLine 2\nLine 3")
            temp_path = f.name
        yield temp_path
        # Видаляємо файл після тесту
        if os.path.exists(temp_path):
            os.unlink(temp_path)

    def test_successful_file_reading(self, temp_file):
        """Тест успішного читання файлу"""
        with FileContextManager(temp_file, 'r') as f:
            content = f.read()
            assert "Test content" in content
            assert FileContextManager.get_statistics()['currently_open'] == 1

        # Після виходу з контексту
        assert FileContextManager.get_statistics()['currently_open'] == 0
        assert FileContextManager.get_statistics()['total_operations'] == 1

    def test_successful_file_writing(self, temp_file):
        """Тест успішного запису в файл"""
        new_content = "New content"

        with FileContextManager(temp_file, 'w') as f:
            f.write(new_content)

        # Перевірка, що контент записався
        with FileContextManager(temp_file, 'r') as f:
            assert f.read() == new_content

        assert FileContextManager.get_statistics()['total_operations'] == 2

    def test_file_not_found_error(self):
        """Тест помилки, коли файл не існує"""
        non_existent = "/path/to/non/existent/file.txt"

        with pytest.raises(FileNotFoundError):
            with FileContextManager(non_existent, 'r') as f:
                f.read()

        # Лічильник не повинен збільшитись для невдалої операції
        assert FileContextManager.get_statistics()['currently_open'] == 0

    def test_exception_in_context_suite(self, temp_file):
        """Тест виключення всередині блоку with"""
        with pytest.raises(ValueError):
            with FileContextManager(temp_file, 'r') as f:
                content = f.read()
                raise ValueError("Test exception")

        # Файл повинен бути закритий
        assert FileContextManager.get_statistics()['currently_open'] == 0

    def test_multiple_concurrent_files(self, temp_file):
        """Тест роботи з кількома файлами одночасно"""
        temp_file2 = temp_file + "_2"
        with open(temp_file2, 'w') as f:
            f.write("File 2")

        try:
            with FileContextManager(temp_file, 'r') as f1:
                assert FileContextManager.get_statistics()['currently_open'] == 1

                with FileContextManager(temp_file2, 'r') as f2:
                    assert FileContextManager.get_statistics()['currently_open'] == 2
                    content1 = f1.read()
                    content2 = f2.read()

                assert FileContextManager.get_statistics()['currently_open'] == 1

            assert FileContextManager.get_statistics()['currently_open'] == 0
            assert FileContextManager.get_statistics()['total_operations'] == 2
        finally:
            if os.path.exists(temp_file2):
                os.unlink(temp_file2)

    def test_binary_mode(self, temp_file):
        """Тест роботи з бінарним режимом"""
        binary_data = b"Binary content"

        with FileContextManager(temp_file, 'wb') as f:
            f.write(binary_data)

        with FileContextManager(temp_file, 'rb') as f:
            assert f.read() == binary_data

    def test_permission_error(self, temp_file):
        """Тест помилки доступу"""
        # Робимо файл тільки для читання
        os.chmod(temp_file, 0o444)

        try:
            with pytest.raises(PermissionError):
                with FileContextManager(temp_file, 'w') as f:
                    f.write("Should fail")
        finally:
            # Відновлюємо права
            os.chmod(temp_file, 0o644)

    @patch('logging.Logger.info')
    @patch('logging.Logger.error')
    def test_logging(self, mock_error, mock_info, temp_file):
        """Тест логування"""
        with FileContextManager(temp_file, 'r') as f:
            content = f.read()

        # Перевіряємо, що були виклики логування
        assert mock_info.called
        assert any("Opening file" in str(call) for call in mock_info.call_args_list)
        assert any("Successfully opened" in str(call) for call in mock_info.call_args_list)
        assert any("Closing file" in str(call) for call in mock_info.call_args_list)