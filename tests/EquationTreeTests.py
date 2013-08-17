import unittest
from forester.EquationTree import EquationTree, Operation

class EquationTreeTests(unittest.TestCase):
    
    def setUp(self):
        self.eq_tree = EquationTree()
        self.op = Operation()
    
    def test_buildSimpleTree(self):
        self.eq_tree.set_operation(op.add)
        