# equation tree

class EquationTree:
    operation = 0
    left_node = 0
    right_node = 0
    
    def __init__ (self, operation, left_node, rigth_node):
        self.operation = operation
        self.left_node = left_node
        self.right_node = rigth_node
        
    def setOperation(self, operation):
        self.operation = operation
        
    def setNodes(self, leftNode, rightNode):
        self.left_node = leftNode
        self.right_node = rightNode
        

class Operation:
    equal = 0
    add = 1
    subtract = 2
    multiply = 3
    divide = 4