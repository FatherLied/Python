class Fraction:
	def __init__(self, num, den):
		self.num = num
		self.den = den

	def __str__(self):
		return "{}/{}".format(self.num, self.den)

	def __repr__(self):
		return self.__str__()


def main():
	test = [Fraction(1,2), Fraction(2,4), Fraction(1,2)]
	print test

	item = test[2]

	test.remove(item)

	print test

	print ""

	control = [1, 2, 1]

	print control

	item = control[2]
	print item

	control.remove(item)

	print control

main()