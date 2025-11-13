import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def test_push_increases_length(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(len(stack), 1)

    def test_pop_returns_last_item(self):
        stack = Stack()
        stack.push(1)
        expected = stack.pop()
        self.assertEqual(expected, 1)

    def test_new_stack_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

    def test_stack_not_empty_after_push(self):
        stack = Stack()
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_peek_returns_last_without_removing(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(len(stack), 1)
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(len(stack), 1)  # перевірка що елемент не видалено


if __name__ == '__main__':
    unittest.main()