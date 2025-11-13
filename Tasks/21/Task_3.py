import pytest
import tempfile
from file_context_manager import FileContextManager


def process_text_file(file_obj):
    """
    Функція для обробки текстових даних з файлу.
    Підраховує статистику тексту.
    """
    content = file_obj.read()

    # Якщо файл відкритий в текстовому режимі
    if isinstance(content, str):
        lines = content.splitlines()
        words = content.split()
        chars = len(content)

        return {
            'lines': len(lines),
            'words': len(words),
            'chars': chars,
            'average_word_length': sum(len(w) for w in words) / len(words) if words else 0
        }
    else:
        # Для бінарних файлів
        return {'bytes': len(content)}


@pytest.fixture
def sample_text_file():
    """
    Pytest fixture, що використовує наш контекстний менеджер
    для створення тестового файлу.
    """
    # Створюємо тимчасовий файл з тестовим контентом
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tf:
        test_content = """Hello World
This is a test file
It contains multiple lines
And some words for testing"""
        tf.write(test_content)
        temp_path = tf.name

    # Використовуємо наш контекстний менеджер
    with FileContextManager(temp_path, 'r') as file_obj:
        yield file_obj

    # Cleanup
    import os
    if os.path.exists(temp_path):
        os.unlink(temp_path)


@pytest.fixture
def empty_file():
    """Fixture для порожнього файлу"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tf:
        temp_path = tf.name

    with FileContextManager(temp_path, 'r') as file_obj:
        yield file_obj

    import os
    if os.path.exists(temp_path):
        os.unlink(temp_path)


class TestTextProcessing:
    """Тестові кейси для функції process_text_file"""

    def test_process_normal_file(self, sample_text_file):
        """Тест обробки звичайного текстового файлу"""
        result = process_text_file(sample_text_file)

        assert result['lines'] == 4
        assert result['words'] == 14
        assert result['chars'] > 0
        assert result['average_word_length'] > 0

    def test_process_empty_file(self, empty_file):
        """Тест обробки порожнього файлу"""
        result = process_text_file(empty_file)

        assert result['lines'] == 0
        assert result['words'] == 0
        assert result['chars'] == 0
        assert result['average_word_length'] == 0

    @pytest.fixture
    def large_file(self):
        """Fixture для великого файлу"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tf:
            # Генеруємо великий контент
            for i in range(1000):
                tf.write(f"Line {i}: Some test content with multiple words\n")
            temp_path = tf.name

        with FileContextManager(temp_path, 'r') as file_obj:
            yield file_obj

        import os
        if os.path.exists(temp_path):
            os.unlink(temp_path)

    def test_process_large_file(self, large_file):
        """Тест обробки великого файлу"""
        result = process_text_file(large_file)

        assert result['lines'] == 1000
        assert result['words'] > 1000
        assert result['chars'] > 0