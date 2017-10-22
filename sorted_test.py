from operator import methodcaller

class Tup:
	def __init__(self, tup):
		self.value = tup[1]
		self.name = tup[0]

	def __str__(self):
		return "{}{}".format(self.name, self.value)

	def __repr__(self):
		return "{}: {}".format(self.name, self.value)

	def add_value(self, num)
		return self.value + num

