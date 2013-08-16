import unittest
from analyzer.Analyzer import Analyzer

class AnalyzerTests(unittest.TestCase):
    
    def setUp(self):
        self.analyzer = Analyzer()
    
    def test_Analyzer_parseAddOperation(self):
        formula = "x + y"
        
        result = self.analyzer.parse(formula)
        
        #self.assertEqual(result.root, , msg) 
        
if __name__ == "__main__":
    unittest.main()