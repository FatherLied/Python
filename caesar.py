class Caesar:

	#	Encryption Function
	def encrypt( self, text, shift ):
		out = ""

		for char in text:
			out += self.shiftedLetter(char, shift)

		return out

	#	Computes for the Shifted Letter (assist Encryption Function)
	def shiftedLetter( self, char, amt ):
		ascii = ord(char)

		# print ascii

		newChar = chr(ascii)

		if (ascii >= 65 and ascii <= 90):
			correction = 65

			newOrd = ( ((ascii - correction) - amt) % 26 ) + correction			
			newChar = chr(newOrd)

		elif (ascii >= 97 and ascii <= 122):
			correction = 97

			newOrd = ( ((ascii - correction) - amt) % 26 ) + correction			
			newChar = chr(newOrd)

		return newChar


# Main?
myCipher = Caesar()

# print (myCipher.encrypt( "Lbh pna rng lbhe bevtvany grkg gvyy fhccyvrf ynfg" , 13))

amount = input("Shift:\t")
text = input("Text:\t")

print ("Result:\t" + myCipher.encrypt( text, amount ))