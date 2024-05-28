import unittest
import functions
import functions_with_errors

class TestFunctions(unittest.TestCase):

    def test_greeting_by_name(self):
        try:
            self.assertEqual(functions.greeting_by_name("John"), "Hello John!")
            print("Test greeting_by_name(name) is Passed")
        except AssertionError:
            print("Test greeting_by_name(name) is Failed")

        try:
            self.assertEqual(functions_with_errors.greeting_by_name("John"), "Hello John!")
            print("Test greeting_by_name(name) is Passed")
        except AssertionError:
            print("Test greeting_by_name(name) is Failed")

    def test_get_symbol_position(self):
        try:
            self.assertEqual(functions.get_symbol_position("hello", "ll"), "Error! Symbol can be string with only one letter")
            print("Test get_symbol_position(text, symbol) when symbol incorrect is Passed")
        except AssertionError:
            print("Test get_symbol_position(text, symbol) when symbol incorrect is Failed")

        try:
            self.assertEqual(functions.get_symbol_position("hello", "e"), 2)
            print("Test get_symbol_position(text, symbol) with success is Passed")
        except AssertionError:
            print("Test get_symbol_position(text, symbol) with success is Failed")

        try:
            self.assertEqual(functions.get_symbol_position("hello", "a"), "Not found")
            print("Test get_symbol_position(text, symbol) when symbol was not found is Passed")
        except AssertionError:
            print("Test get_symbol_position(text, symbol) when symbol was not found is Failed")

        


        try:
            self.assertNotEqual(functions_with_errors.get_symbol_position("hello", "ll"), "Error! Symbol can be string with only one letter")
            print("Test get_symbol_position(text, symbol) when symbol incorrect is Passed")
        except AssertionError:
            print("Test get_symbol_position(text, symbol) when symbol incorrect is Failed")

        try:
            self.assertNotEqual(functions_with_errors.get_symbol_position("hello", "e"), 2)
            print("Test get_symbol_position(text, symbol) with success is Passed")
        except AssertionError:
            print("Test get_symbol_position(text, symbol) with success is Failed")

        try:
            self.assertNotEqual(functions_with_errors.get_symbol_position("hello", "a"), "Not found")
            print("Test get_symbol_position(text, symbol) when symbol was not found is Passed")
        except AssertionError:
            print("Test get_symbol_position(text, symbol) when symbol was not found is Failed")


    def test_merge(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}



        try:
            self.assertEqual(dict1, {'a': 1, 'b': 2})  
            print("Test merge(dict1, dict2) dict1 immutability is Passed")
        except AssertionError:
            print("Test merge(dict1, dict2) dict1 immutability is Failed")


        try:
            result = functions_with_errors.merge(dict1, dict2)
            self.assertEqual(result, {'a': 1, 'b': 3, 'c': 4})
            print("Test merge(dict1, dict2) is Passed")
        except AssertionError:
            print("Test merge(dict1, dict2) is Failed")

        try:
            self.assertNotEqual(dict1, {'a': 1, 'b': 2})  
            print("Test merge(dict1, dict2) dict1 immutability is Passed")
        except AssertionError:
            print("Test merge(dict1, dict2) dict1 immutability is Failed")

        try:
            result = functions.merge(dict1, dict2)
            self.assertEqual(result, {'a': 1, 'b': 3, 'c': 4})
            print("Test merge(dict1, dict2) is Passed")
        except AssertionError:
            print("Test merge(dict1, dict2) is Failed")

if __name__ == "__main__":
    unittest.main()






