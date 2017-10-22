#ord('a')   ==  int value of char
#chr(97)    ==  char value of int
#len("String")  ==  gets length of string

#str(1)     ==  turns int to string (for concatenation)
#int("12")  ==  turns string to int

#input("Enter char: ")  ==  receives input after text

#[1,2,3].index(1)   ==  finds index of a collection
#"{} {}".format("Hello","World")    ==  Fills strings in {}

#open("File.in")    ==  opens a file
#<file>.read(<size>)    ==  reads the whole file (if <size> is not filled in)
#<file>.readline()  ==  reads a line of the file

#<list>.append(item)  ==  adds item to the end of the list
#<list>.extend(list)  ==  adds each item of the target list to the source list

#<str>.splitlines()  == splits string into lines; crossplatform removes '/r/n', '/n' or '/r'
#<str>.split(delimiter)  ==  splits strings into an array of strings using delimiter
"""
~~ Advanced ~~

##  Clear console window
import os
os.system('cls' if os.name == 'nt' else 'clear')

##  Parse all lone numbers in a string (separated by non-characters) into a list
[int(s) for s in str.split() if s.isdigit()]

##  Reverse a string
string[::-1]

"""

"""
Imports:

import random
{
    ### Library for generating pseudo-random numbers

    # Important Functions:

    random.random():
        Return the next random floating point number in the range [0.0, 1.0).

    random.randint(a, b):
        Return a random integer N such that a <= N <= b.

    random.choice(seq)
        Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.
}

import operator
{
    ### Library for standard operators as functions

    # Important Functions:

    operator.attrgetter(attr):
        Return a callable object that fetches attr from its operand.

    operator.attrgetter(*attrs):
        Returns a tuple of attributes if multiple attributes are requested.

    operator.itemgetter(item):
        Return a callable object that fetches item from its operand using the operand’s __getitem__() method.

    operator.itemgetter(*items):
        Returns a tuple of lookup values if multiple items are specified.
}


"""