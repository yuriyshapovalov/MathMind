# equation tree

class Equation:
    root_node = 0
    semantic = 0
        
    def set_nodes(self, leftNode, rightNode):
        self.left_node = leftNode
        self.right_node = rightNode
        
    def has_nodes(self, node):
        return node.left_node != 0 and node.right_node != 0  
     
        
class EqNode:
    value = 0
    left_node
    rigth_node
    
    def set_value(self, value):
        self.value = value
        
    def set_left_node(self, node):
        self.left_node = node
    
    def set_right_node(self, node):
        self.right_node = node
        
    

class Operation:
    equal = 0
    add = 1
    subtract = 2
    multiply = 3
    divide = 4