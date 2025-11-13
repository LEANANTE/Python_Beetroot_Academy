import logging
from typing import Optional, Any
from datetime import datetime

# Налаштування логування
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


class FileContextManager:
    """
    Власний контекстний менеджер для роботи з файлами
    з функціоналом лічильника та логування.
    """

    # Класова змінна для підрахунку відкритих файлів
    _open_count = 0
    _total_operations = 0

    def __init__(self, filename: str, mode: str = 'r', encoding: str = 'utf-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file_obj = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self._operation_id = None

    def __enter__(self):
        """Метод входу в контекст"""
        try:
            # Збільшуємо лічильники
            FileContextManager._open_count += 1
            FileContextManager._total_operations += 1
            self._operation_id = FileContextManager._total_operations

            # Логування початку операції
            self.logger.info(
                f"Opening file: {self.filename} in mode: {self.mode} "
                f"(Operation #{self._operation_id}, Currently open: {self._open_count})"
            )

            # Відкриваємо файл
            if 'b' in self.mode:
                self.file_obj = open(self.filename, self.mode)
            else:
                self.file_obj = open(self.filename, self.mode, encoding=self.encoding)

            self.logger.info(f"Successfully opened: {self.filename}")
            return self.file_obj

        except Exception as e:
            # Зменшуємо лічильник у випадку помилки
            FileContextManager._open_count -= 1
            self.logger.error(f"Failed to open {self.filename}: {str(e)}")
            raise

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """
        Метод виходу з контексту.
        Обробляє всі види виключень згідно з документацією.
        """
        # Зменшуємо лічильник відкритих файлів
        FileContextManager._open_count -= 1

        # Логування виходу
        if exc_type is None:
            self.logger.info(
                f"Closing file: {self.filename} "
                f"(Operation #{self._operation_id}, Remaining open: {self._open_count})"
            )
        else:
            self.logger.error(
                f"Exception occurred with {self.filename}: "
                f"{exc_type.__name__}: {exc_value}"
            )

        # Закриваємо файл, якщо він був відкритий
        if self.file_obj:
            try:
                self.file_obj.close()
                self.logger.info(f"File {self.filename} closed successfully")
            except Exception as close_error:
                self.logger.error(f"Error closing file {self.filename}: {close_error}")
                # Якщо була попередня помилка, не перезаписуємо її
                if exc_type is None:
                    raise close_error

        # Повертаємо False, щоб не придушувати виключення
        # (або True, якщо хочемо придушити певні типи виключень)
        return False

    @classmethod
    def get_statistics(cls):
        """Отримати статистику використання"""
        return {
            'currently_open': cls._open_count,
            'total_operations': cls._total_operations
        }

    @classmethod
    def reset_statistics(cls):
        """Скинути статистику"""
        cls._open_count = 0
        cls._total_operations = 0