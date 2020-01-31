import unittest
from app.fibonacci_program import return_nth_fib_number


class Test_Nth_Fib(unittest.TestCase):
    def test_correct_output(self):
        self.assertEqual(return_nth_fib_number(2), 1)

    def test_input_is_a_number(self):
        self.assertEqual(type(return_nth_fib_number(2)), int)
