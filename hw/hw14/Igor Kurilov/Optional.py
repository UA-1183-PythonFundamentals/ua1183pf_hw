import unittest
from functions import greeting_by_name as f_greeting_by_name, get_symbol_position as f_get_symbol_position, merge as f_merge
from functions_with_errors import greeting_by_name as fe_greeting_by_name, get_symbol_position as fe_get_symbol_position, merge as fe_merge

class TestFunctions(unittest.TestCase):

    def test_greeting_by_name(self):
        self.assertEqual(f_greeting_by_name("Alice"), "Hello Alice!")
        self.assertEqual(fe_greeting_by_name("Alice"), "Hello name!")

    def test_get_symbol_position(self):
        text = "Hello, World!"
        symbol = ","
        self.assertEqual(f_get_symbol_position(text, symbol), 6)
        self.assertEqual(fe_get_symbol_position(text, symbol), text.find(symbol))

        # Test case for incorrect symbol
        self.assertEqual(f_get_symbol_position(text, "test"), "Error! Symbol can be string with only one letter")
        self.assertEqual(fe_get_symbol_position(text, "test"), "Error! Symbol can be string with only one letter")

        # Test case when symbol not found
        self.assertEqual(f_get_symbol_position(text, "?"), "Not found")
        self.assertEqual(fe_get_symbol_position(text, "?"), -1)

    def test_merge(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}

        # Test immutability of input dictionaries
        f_merged_dict = f_merge(dict1, dict2)
        self.assertNotEqual(dict1, f_merged_dict)
        self.assertNotEqual(dict2, f_merged_dict)

        fe_merged_dict = fe_merge(dict1, dict2)
        self.assertEqual(dict1, fe_merged_dict)  # This test will fail because of the mistake in the function
        self.assertEqual(dict2, fe_merged_dict)  # This test will fail because of the mistake in the function

        # Test correctness of merged dictionaries
        self.assertEqual(f_merged_dict, {'a': 1, 'b': 2, 'c': 3, 'd': 4})
        self.assertEqual(fe_merged_dict, {'a': 1, 'b': 2, 'c': 3, 'd': 4})  # This test will fail because of the mistake in the function

if __name__ == "__main__":
    unittest.main()
