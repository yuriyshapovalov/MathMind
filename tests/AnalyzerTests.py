import unittest
from analyzer.Analyzer import Analyzer

class AnalyzerTests(unittest.TestCase):
    
    def setUp(self):
        self.analyzer = Analyzer()
    
    def test_Analyzer_parseFormula(self):
        self.assertTrue(self.analyzer.returnTrueForTest(), "Done")
        
if __name__ == "__main__":
    unittest.main()