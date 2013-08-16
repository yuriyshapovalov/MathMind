# Parser

class Parser:
	operation_stack = []
	variable_stack = []

	def parse(formula):
		f_tuple = parse(formula)

		for element in f_tuple:
			if (element == '+' or element == '-' or element == '*' or element == '/'):
				operation_stack.push(element)
			else:
				variable_stack.push(element)



