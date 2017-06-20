class Cryptor:
	table = [['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],	# (0,0) = A
			 ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A'],
			 ['C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B'],
			 ['D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C'],
			 ['E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D'],
			 ['F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E'],
			 ['G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F'],
			 ['H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G'],
			 ['I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H'],
			 ['J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I'],
			 ['K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J'],
			 ['L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K'],
			 ['M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L'],
			 ['N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M'],
			 ['O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N'],
			 ['P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O'],
			 ['Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'],
			 ['R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q'],
			 ['S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R'],
			 ['T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S'],
			 ['U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T'],
			 ['V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U'],
			 ['W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V'],
			 ['X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W'],
			 ['Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X'],
			 ['Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']]

	#def __init__(self):

	def get(self, row, column):
		return self.table[row][column]

	def encrypt(self, text, code):
		out = ""

		index = 0

		for char in text:
			out += self.get( self.trans(char) , self.trans(code[index % len(code)]) )

			index += 1

		return out

	def decrypt(self, crypt, code):
		out = ""

		index = 0

		for char in crypt:
			char = self.spose( self.trans(char) )	# indexToChar

			cIndex = self.trans(code[index % len(code)])  # charToIndex

			out += self.spose( self.table[ cIndex % 26 ].index(char) )

			index += 1

		return out

	def spose(self, index):		# Transposes indices to their character equivalents
		return chr(index + 65)

	def trans(self, char):		# Transposes characters to their index equivalents
		if(char == 'A' or char == 'a'):
			return 0
		if(char == 'B' or char == 'b'):
			return 1
		if(char == 'C' or char == 'c'):
			return 2
		if(char == 'D' or char == 'd'):
			return 3
		if(char == 'E' or char == 'e'):
			return 4
		if(char == 'F' or char == 'f'):
			return 5
		if(char == 'G' or char == 'g'):
			return 6
		if(char == 'H' or char == 'h'):
			return 7
		if(char == 'I' or char == 'i'):
			return 8
		if(char == 'J' or char == 'j'):
			return 9
		if(char == 'K' or char == 'k'):
			return 10
		if(char == 'L' or char == 'l'):
			return 11
		if(char == 'M' or char == 'm'):
			return 12
		if(char == 'N' or char == 'n'):
			return 13
		if(char == 'O' or char == 'o'):
			return 14
		if(char == 'P' or char == 'p'):
			return 15
		if(char == 'Q' or char == 'q'):
			return 16
		if(char == 'R' or char == 'r'):
			return 17
		if(char == 'S' or char == 's'):
			return 18
		if(char == 'T' or char == 't'):
			return 19
		if(char == 'U' or char == 'u'):
			return 20
		if(char == 'V' or char == 'v'):
			return 21
		if(char == 'W' or char == 'w'):
			return 22
		if(char == 'X' or char == 'x'):
			return 23
		if(char == 'Y' or char == 'y'):
			return 24
		if(char == 'Z' or char == 'z'):
			return 25


myClass = Cryptor()

# encrypted = myClass.encrypt("PluralsightSecurityPlusRocks","comptiacomptiacomptiacomptia")

# print encrypted
# print (encrypted == "RZGGTTSKUTILMCWFUIRXLWGDDVSS")

decrypted = myClass.decrypt("RZGGTTSKUTILMCWFUIRXLWGDDVSS","comptiacomptiacomptiacomptia")

print decrypted
print (decrypted == "PLURALSIGHTSECURITYPLUSROCKS")

opCode = ""
message = ""
passkey = ""
encrypt = "encrypt"
decrypt = "decrypt"
exit = "exit"

while(opCode != "exit"):
	opCode = input("[encrypt/decrypt/exit]: ")

	# print ("\n")

	if(opCode == "encrypt"):
		message = input("\nDecrypted message: ")
		passkey = input("PassKey: ")

		print ("\nEncrypted Message: " + myClass.encrypt(message,passkey))
	elif(opCode == "decrypt"):
		message = input("\nEncrypted message: ")
		passkey = input("PassKey: ")

		print ("\nDecrypted Message: " + myClass.decrypt(message,passkey))
	elif(opCode == "exit"):
		print ("\nGoodbye.")
	else:
		print ("\n<<Invalid Input>>")

	print ("\n")

	lastKey = passkey
	lastMessage = message
