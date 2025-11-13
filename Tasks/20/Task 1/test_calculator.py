import unittest
from calculator import make_operation


class TestMakeOperation(unittest.TestCase):

    def test_addition_basic(self):
        """Тест базового додавання"""
        self.assertEqual(make_operation('+', 7, 7, 2), 16)
        self.assertEqual(make_operation('+', 1), 1)
        self.assertEqual(make_operation('+', 0, 0, 0), 0)

    def test_addition_negative_numbers(self):
        """Тест додавання з негативними числами"""
        self.assertEqual(make_operation('+', -5, 10, -3), 2)
        self.assertEqual(make_operation('+', -1, -2, -3), -6)

    def test_subtraction_basic(self):
        """Тест віднімання"""
        self.assertEqual(make_operation('-', 5, 5, -10, -20), 30)
        self.assertEqual(make_operation('-', 100, 25, 25), 50)
        self.assertEqual(make_operation('-', 10), 10)

    def test_multiplication_basic(self):
        """Тест множення"""
        self.assertEqual(make_operation('*', 7, 6), 42)
        self.assertEqual(make_operation('*', 2, 3, 4), 24)
        self.assertEqual(make_operation('*', -2, 3), -6)

    def test_multiplication_with_zero(self):
        """Тест множення з нулем"""
        self.assertEqual(make_operation('*', 0, 100, 200), 0)
        self.assertEqual(make_operation('*', 5, 0, 3), 0)

    def test_float_numbers(self):
        """Тест з дробовими числами"""
        self.assertAlmostEqual(make_operation('+', 1.5, 2.5), 4.0)
        self.assertAlmostEqual(make_operation('*', 2.5, 2), 5.0)

    def test_invalid_operation(self):
        """Тест неправильної операції"""
        with self.assertRaises(TypeError) as context:
            make_operation('/', 1, 2)
        self.assertIn("not supported", str(context.exception))

        with self.assertRaises(TypeError):
            make_operation('%', 1, 2)

    def test_non_numeric_argument(self):
        """Тест з нечисловим аргументом"""
        with self.assertRaises(ValueError) as context:
            make_operation('+', 1, 2, "string")
        self.assertIn("not a number", str(context.exception))

        with self.assertRaises(ValueError):
            make_operation('+', 1, [2], 3)

    def test_no_arguments(self):
        """Тест без чисел"""
        with self.assertRaises(ValueError) as context:
            make_operation('+')
        self.assertIn("At least one number", str(context.exception))

    def test_single_argument(self):
        """Тест з одним аргументом"""
        self.assertEqual(make_operation('+', 5), 5)
        self.assertEqual(make_operation('-', 5), 5)
        self.assertEqual(make_operation('*', 5), 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)