import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from ccg.combinator import UndirectedFunctionApplication, combine_coverage, print_coverage

class MockResult:
    def substitute(self, subs):
        return f"Result with substitution {subs}"

class MockArgument:
    def can_unify(self, other_argument):
        if other_argument == 10:
            return {"example_substitution": "value"}
        return None

class MockFunction:
    def __init__(self, func):
        self.func = func

    def is_function(self):
        return True

    def arg(self):
        return MockArgument()

    def res(self):
        return MockResult()

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
    
class NotFunction:
    def __init__(self, func):
        self.func = func

    def is_function(self):
        return False

    def arg(self):
        return MockArgument()

    def res(self):
        return MockResult()

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

class TestUndirectedFunctionApplication(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        print("\n \nPrinting Coverage Summary for Function Token.str:")
        print_coverage()

    def test_combine(self):
        ufa = UndirectedFunctionApplication()
        argument1 = 10
        def functionToPass(num):
            return num * 2
        mock_function = MockFunction(functionToPass)

        result = next(ufa.combine(mock_function, argument1), None)
        self.assertIsNotNone(result)
        self.assertIn("Result with substitution", result)

    def test_is_function(self):
        ufa = UndirectedFunctionApplication()
        argument1 = 10
        def functionToPass(num):
            return num * 2
        mock_function = MockFunction(functionToPass)
        self.assertTrue(ufa.combine(mock_function, argument1))

    def test_is_not_function(self):
        ufa = UndirectedFunctionApplication()
        argument1 = 10
        def functionToPass(num):
            return num * 2
        not_function = NotFunction(functionToPass)
        print(not_function.is_function())
        self.assertEqual(ufa.combine(not_function, argument1), False)

    def test_arg_can_unify(self):
        def functionToPass(num):
            return num * 2
        mock_function = MockFunction(functionToPass)
        argument = mock_function.arg()
        self.assertIsNotNone(argument.can_unify(10))
        self.assertIsNone(argument.can_unify(5))

    def test_result_substitution(self):
        mock_result = MockResult()
        substitution = {"key": "value"}
        expected_result = f"Result with substitution {substitution}"
        self.assertEqual(mock_result.substitute(substitution), expected_result)
    

if __name__ == '__main__':
    unittest.main()