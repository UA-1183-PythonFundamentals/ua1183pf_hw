import unittest
from functions import greeting_by_name, get_symbol_position, merge
from functions_with_errors import greeting_by_name as greeting_by_name_err, \
    get_symbol_position as get_symbol_position_err, merge as merge_err


class TestFunctions(unittest.TestCase):
    def test_greeting_by_name(self):
        self.assertEqual(greeting_by_name("Alice"), "Hello Alice!")
        self.assertEqual(greeting_by_name_err("Alice"), "Hello Alice!")  # Error not present

    def test_get_symbol_position(self):
        self.assertEqual(get_symbol_position("hello", "o"), 5)
        self.assertEqual(get_symbol_position("hello", "z"), "Not found")
        self.assertEqual(get_symbol_position("hello", "ll"), "Error! Symbol can be string with only one letter")
        self.assertEqual(get_symbol_position_err("hello", "o"), 4)  # Error not present

    def test_merge(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        self.assertEqual(merge(dict1, dict2), {'a': 1, 'b': 3, 'c': 4})
        self.assertEqual(merge_err(dict1, dict2), {'a': 1, 'b': 3, 'c': 4})  # Error not present


if __name__ == '__main__':
    unittest.main()
