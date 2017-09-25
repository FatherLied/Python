class Operation:
	def __init__(self):
		pass

	def addition(self):
		print "1 + 1 = 2"

	def subtraction(self):
		print "1 - 1 = 0"

	def multiplication(self):
		print "1 * 1 = 1"

	def operate(self, mode):
		switch = {
			"add":self.addition,
			"sub":self.subtraction,
			"mul":self.multiplication
		}

		switch[mode]()

test = Operation()

test.operate("sub")