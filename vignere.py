class Vignere:
    # Vignere Encryption/Decryption
    table = [['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'], # (0,0) = A
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

    def encrypt (self , text, key, shift):
        out = ""
        decryptedKey = self.deCaesar(key, shift)
        # print decryptedKey

        index = 0
        for char in text:
            if ( (char >= "a" and char <= "z") or (char >= "A" and char <= "Z") ):
                out += self.vignereTable(char, key[index])
                # print key[index]

                index = (index + 1) % len(key)
            else:
                out += char

        return out

    def decrypt (self , text, key, shift):
        out = ""
        decryptedKey = self.deCaesar(key, shift)
        # print decryptedKey

        index = 0
        for char in text:
            if ( (char >= "a" and char <= "z") or (char >= "A" and char <= "Z") ):
                out += self.vignereRev(char, decryptedKey[index])
                # print key[index]

                index = (index + 1) % len(key)
            else:
                out += char

        return out


    def indexToChar (self, index):
        if (index < 26):
            return chr( index + 65)
        else:
            return chr( (index - 26) + 97)

    def charToIndex (self, char):

        if (char >= "A" and char <= "Z"):
            return ord(char) - 65
        elif (char >= "a" and char <= "z"):
            return (ord(char) - 97) + 26

    def vignereTable (self, char, key):
        keyIndex = self.charToIndex(key)
        charIndex = self.charToIndex(char)

        # print (key + "[" + str(keyIndex) + "]")
        # print (char + "[" + str(charIndex) + "]")
        # print "\n"

        newChar = self.table[charIndex % 26][keyIndex % 26]

        if (charIndex >= 26):
            newChar = chr( ord(newChar) + 32 )

        # print ("[" + char + "][" + key + "] : " + newChar + "\n")

        return newChar

    def vignereRev(self, char, key):
        keyIndex = self.charToIndex(key)
        charQuery = char
        lower = False

        if (char >= "a" and char <= "z"):
            charQuery = chr( ord(char) - 32 )
            lower = True

        charIndex = self.table[keyIndex % 26].index(charQuery)

        newChar = self.indexToChar(charIndex)

        if(lower):
            newChar = chr( ord(newChar) + 32 )

        return newChar

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #   Caesar Decryption
    def deCaesar (self, text, shift):
        out = ""

        for char in text:
            out += self.shiftedLetter(char, shift)

        return out

    #   Computes for the Shifted Letter (assists Encryption Function)
    def shiftedLetter( self, char, amt ):
        ascii = ord(char)

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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# Main
myClass = Vignere()

# print myClass.decrypt("QQU fhe mvh fsg lo fqt bespsjl xtm dautvqcejcu me klwcr", "qaylbyjzmfckgy", 24)
# print myClass.deCaesar("qaylbyjzmfckgy", 24)

# print myClass.encrypt("you see but you do not observe the distinction is clear", "scandalbohemia", 0)
# print myClass.decrypt("QQU fhe mvh fsg lo fqt bespsjl xtm dautvqcejcu me klwcr", "scandalbohemia", 0)
# print myClass.encrypt("you see but you do not observe the distinction is clear", "qaylbyjzmfckgy", 24)
# print myClass.encrypt("Mandaue", "Humba", 0)

fileName = input("File Name: ")

with open(fileName) as f:
    lines = f.read().split("\n")

# for line in lines:
    # print line

# lines[0] == shift amount
# lines[1] == encrypted message
# lines[2] == passphrase

print "Decrypted Message:\n\t" + myClass.decrypt(lines[1], lines[2], int(lines[0]))
