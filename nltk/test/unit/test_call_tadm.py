
import unittest
import sys
import os

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '/Users/junlee/sep/nltk_SEP_group120/nltk'))
sys.path.insert(0, module_path)

from classify.tadm import call_tadm, branch_coverage, print_coverage, reset_coverage, test_tadm_bin_generator

class TestCallTadm(unittest.TestCase):

    def setUp(self):
        reset_coverage()
        global _tadm_bin
        _tadm_bin = None
    
    def test_call_tadm_typeError_T(self):
        print("test_call_tadm_typeError_T")
        try:
            call_tadm("hello")
            print_coverage()
        except Exception as e:
            print_coverage()
        
        self.assertTrue(branch_coverage["call_tadm_args_typeError"])
        
        print("------------")

    def test_call_tadm_typeMatched_bin_None(self):
        print("test_call_tadm_typeMatched_bin_None")
        test_tadm_bin_generator(None)
        try:
            call_tadm(["hi"])
            print_coverage()
        except Exception as e:
            print_coverage()

        self.assertTrue(branch_coverage["call_tadm_args_typeMatched"])
        self.assertTrue(branch_coverage["call_tadm_tadm_bin_none"])
        
        print("------------")

    def test_call_tadm_bin_NOT_None_Failure(self):
        print("test_call_tadm_bin_NOT_None_Failure")
        test_tadm_bin_generator("/bin/ls")
        try:
            call_tadm(["/nonexistent_directory"])
            print_coverage()
        except Exception:
            print_coverage()

        self.assertTrue(branch_coverage["call_tadm_args_typeMatched"])
        self.assertTrue(branch_coverage["call_tadm_tadm_bin_NOT_none"])
        self.assertTrue(branch_coverage["call_tadm_failure"])
        
        print("------------")

    def test_call_tadm_bin_NOT_None_Success(self):
        print("test_call_tadm_bin_NOT_None_Success")
        test_tadm_bin_generator("/bin/echo" )
        try:
            call_tadm(["hello"])
            print_coverage()
        except Exception as e:
            print_coverage()

        self.assertTrue(branch_coverage["call_tadm_args_typeMatched"])
        self.assertTrue(branch_coverage["call_tadm_tadm_bin_NOT_none"])
        self.assertTrue(branch_coverage["call_tadm_success"])
        
        print("------------")
   

if __name__ == '__main__':
    unittest.main()
