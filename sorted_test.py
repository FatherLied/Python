from operator import methodcaller

class Tup:
	def __init__(self, tup):
		self.value = tup[1]
		self.name = tup[0]

	def __str__(self):
		return "{}{}".format(self.name, self.value)

	def __repr__(self):
		return "{}: {}".format(self.name, self.value)

	def add_value(self, num):
		return self.value + num

classic = [('a', 6), ('b', 3), ('c', 4), ('d', 8), ('e', 1)]

test = []

for item in classic:
	test.append(Tup(item))

print("Unsorted: {}".format(test))

x = 5

test = sorted(test, key = methodcaller('add_value', x))

print("Sorted: {}".format(test))