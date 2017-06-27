class Parent():
	toggled = False
	count = 0

	@classmethod
	def toggle(cls):
		if cls.toggled:
			cls.count += 5
			cls.toggled = False
		else:
			cls.count += 5
			cls.toggled = True

	def __init__(self):
		self.name = "Parent"

	def isToggled(self):
		self.count += 1
		print "{} is toggled? {}".format(self.name, self.toggled)

	def yellCount(self):
		return "{}: {}".format(self.name,self.count)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Son(Parent):
	def __init__(self):
		self.count += 2
		self.name = "Son"

	def yell(self):
		# self.count += 1
		print "I am more loved than my sister!!!"

class Daughter(Parent):
	def __init__(self):
		self.count += 2
		self.name = "Daughter"

	def yell(self):
		# self.count += 2
		print "I am more loved than my brother!!!"

def main():
	dad = Parent()
	mom = Parent()
	boy = Son()
	girl = Daughter()

	dad.isToggled()
	mom.isToggled()
	boy.isToggled()
	girl.isToggled()

	print "\n"

	boy.toggle()
	dad.toggle()

	dad.isToggled()
	mom.isToggled()
	boy.isToggled()
	girl.isToggled()

	# print "\n"

	# boy.yell()
	# girl.yell()

	print "\n"

	# dad.yell()
	print dad.yellCount()
	print mom.yellCount()
	# print boy.yellCount()
	# print girl.yellCount()

	pass

main()