import unittest
import sys
import os

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '/Users/niekbremer/nltk/nltk'))
sys.path.insert(0, module_path)

from ccg.lexicon import branch_coverage_str, print_coverage_str, Token  

class TestTokenStr(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.reset_coverage()

    @classmethod
    def tearDownClass(cls):
        print("\n \nPrinting Coverage Summary for Function Token.str:")
        print_coverage_str()

    @classmethod
    def reset_coverage(cls):
        for key in branch_coverage_str:
            branch_coverage_str[key] = False

    def test_str_with_semantics(self):
        token = Token(token="eat", categ="S\\var[pl]/var", semantics="\\x y.eat(x,y)")
        result = str(token)
        expected = "S\\var[pl]/var {\\x y.eat(x,y)}"
        self.assertEqual(result, expected)
        self.assertTrue(branch_coverage_str["branch_if"])

    def test_str_without_semantics(self):
        token = Token(token="eat", categ="S\\var[pl]/var")
        result = str(token)
        expected = "S\\var[pl]/var"
        self.assertEqual(result, expected)
        self.assertTrue(branch_coverage_str["branch_else"])

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestTokenStr)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
