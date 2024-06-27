
import unittest
import sys
import os

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '/Users/junlee/sep/nltk_SEP_group120/nltk'))
sys.path.insert(0, module_path)

from nltk import config_megam

from classify.rte_classify_testCase_version import rte_classifier, branch_coverage, print_coverage, reset_coverage
from nltk.corpus import rte as rte_corpus


class TestRTEClassifierOnly(unittest.TestCase):

    def setUp(self):
        reset_coverage()
    
    def test_rte_classification_without_megam(self):
        # Use a sample size for unit testing, since we
        # don't need to fully train these classifiers
        try:
            clf = rte_classifier("IIS", sample_N=100)
            clf = rte_classifier("GIS", sample_N=100)
            self.assertTrue(branch_coverage["branch_if_sample_N_not_none"])
            self.assertTrue(branch_coverage["branch_elif_algorithm_GIS_IIS"])
            print("test_rte_classification_without_megam")
            print_coverage()
        except Exception as e:
            print(e)
            print_coverage()
    
    def test_rte_classification_with_megam(self):
        try:
            clf = rte_classifier("megam", sample_N=100)
            print("test_rte_classification_with_megam")
            print_coverage()
        except Exception as e:
            print(e)
            print("test_rte_classification_with_megam")
            print_coverage()
            
        self.assertTrue(branch_coverage["branch_if_sample_N_not_none"])
        self.assertTrue(branch_coverage["branch_if_algorithm_megam"])

        
    # above test completes 3 out of 5 branches thus adding two extra to fullfil 100%
    
    def test_rte_classification_sampleN_None(self):
        
        clf = rte_classifier("GIS", None)
        self.assertTrue(branch_coverage["branch_else_sample_N_none"])
        self.assertTrue(branch_coverage["branch_elif_algorithm_GIS_IIS"])
        print("test_rte_classification_sampleN_None")
        print_coverage()
            
        
    def test_rte_classification_unsupported_algorithm(self):
        
        with self.assertRaises(Exception):
            clf = rte_classifier("ALGO", sample_N=100)
        self.assertTrue(branch_coverage["branch_if_sample_N_not_none"])
        self.assertTrue(branch_coverage["branch_else_algorithm_error"])
        print("test_rte_classification_unsupported_algorithm")
        print_coverage()
        

if __name__ == '__main__':
    unittest.main()
