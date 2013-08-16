# Parser

class Analyzer:
	operation_stack = []
	variable_stack = []
	
	operation_tree = 0

	def parse_formula(self, formula):
		f_tuple = parse(formula)

		for element in f_tuple:
			if (element == '+' or element == '-' or element == '*' or element == '/'):
				operation_stack.push(element)
			else:
				variable_stack.push(element)
				
		return operation_tree
	
	def returnTrueForTest(self):
		return True


