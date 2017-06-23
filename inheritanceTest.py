class Parent():
	toggled = False

	@classmethod
	def toggle(cls):
		if cls.toggled:
			cls.toggled = False
		else:
			cls.toggled = True

	def __init__(self):
		self.name = "Parent"

	def isToggled(self):
		print "{} is toggled? {}".format(self.name, self.toggled)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Son(Parent):
	def __init__(self):
		self.name = "Son"

	def yell(self):
		print "I am more loved than my sister!!!"

class Daughter(Parent):
	def __init__(self):
		self.name = "Daughter"

	def yell(self):
		print "I am more loved than my brother!!!"

def main():
	dad = Parent()
	boy = Son()
	girl = Daughter()

	dad.isToggled()
	boy.isToggled()
	girl.isToggled()

	print "\n"

	boy.toggle()

	dad.isToggled()
	boy.isToggled()
	girl.isToggled()

	print "\n"

	boy.yell()
	girl.yell()

	# dad.yell()

	pass

main()