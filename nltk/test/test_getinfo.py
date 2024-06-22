import unittest
import sys
import os

# Add the path to the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '/Users/niekbremer/nltk/nltk')))
from decorators import getinfo, branch_coverage_getinfo, print_coverage_getinfo

class TestGetInfo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.reset_coverage()

    @classmethod
    def tearDownClass(cls):
        print("Printing Coverage Summary:")
        print_coverage_getinfo()

    @classmethod
    def reset_coverage(cls):
        for key in branch_coverage_getinfo:
            branch_coverage_getinfo[key] = False

    def test_getinfo_with_varargs(self):
        def example_function(self, x=1, *args):
            pass
        info = getinfo(example_function)
        self.assertIn("*args", info["signature"])
        self.assertTrue(branch_coverage_getinfo["branch_varargs_if"])

    def test_getinfo_with_varkwargs(self):
        def example_function(self, x=1, **kwargs):
            pass
        info = getinfo(example_function)
        self.assertIn("**kwargs", info["signature"])
        self.assertTrue(branch_coverage_getinfo["branch_varkwargs_if"])

    def test_getinfo_with_closure(self):
        def outer():
            x = 1
            def inner():
                return x
            return inner
        func = outer()
        info = getinfo(func)
        self.assertIsNotNone(info["closure"])
        self.assertTrue(branch_coverage_getinfo["branch_hasattr_if"])

    def test_getinfo_without_closure(self):
        def example_function(self, x=1):
            pass
        info = getinfo(example_function)
        self.assertIsNone(info["closure"])
        self.assertTrue(branch_coverage_getinfo["branch_hasattr_if"])

    def test_getinfo_with_all(self):
        def example_function(self, x=1, *args, **kwargs):
            pass
        info = getinfo(example_function)
        self.assertIn("*args", info["signature"])
        self.assertIn("**kwargs", info["signature"])
        self.assertTrue(branch_coverage_getinfo["branch_varargs_if"])
        self.assertTrue(branch_coverage_getinfo["branch_varkwargs_if"])

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestGetInfo)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
