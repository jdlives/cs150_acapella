import sys
import string

filename = "test.txt"
f = open("test.txt", 'r')

def lexer(token):

	checkIdentifier = 0
	checkNumber = 0
	checkNotIdentifier = 0

	print(token)

	keywords = "play pause stop repeat chorus duet solo cue final prelude postlude interlude"
	keyword = keywords.split()

	oneCharSymbols = "= ( ) [ ] rewind forward + - * / % ! duet solo > < ,"
	symbol1 = oneCharSymbols.split()

	twoCharSymbols = "== != >= <= += -= *= /="
	symbol2 = twoCharSymbols.split()

	datatypes = "Do Re Mi Fa So La Ti lyrics verse album albums symphony symphonies playlist"
	datatype = datatypes.split()

	identifiersHead = string.letters
	identifiersTail = string.letters + string.digits + "_"

	numbersHead = string.digits + "."
	numbersTail = string.digits + "." + ""

	for i in range(0, len(token)):
		for j in range(0, len(numbersHead)):
			if (token[i] == numbersHead[j]):
				for m in range(0, len(token)):
					for n in range(0, len(numbersTail)):
						if (token[m] == numbersTail[n]):
							checkNumber = 1
		
	if (checkNumber == 1):
		print("NUMBER")


	for i in range(0,len(keyword)):
		if token == keyword[i]:
			print("KEYWORD")
			checkNotIdentifier = 1

	for i in range(0, len(symbol1)):
		if token == symbol1[i]:
			print("ONE-CHAR OPERATOR")

	for i in range(0, len(symbol2)):
		if token == symbol2[i]:
			print("TWO-CHAR OPERATOR")

	for i in range(0, len(datatype)):
		if token == datatype[i]:
			print("DATA TYPE")
			checkNotIdentifier = 1

	for i in range(0, len(token)):
		for j in range(0, len(identifiersHead)):
			if (token[i] == identifiersHead[j]):
				for m in range(i, len(token)):
					for n in range(0, len(identifiersTail)):
						if (token[m] == identifiersTail[n]):
							checkIdentifier = 1
				break;

	if (checkIdentifier == 1 and checkNotIdentifier == 0):
		print("IDENTIFIER")




def scanner():
	global nextChar
	nextChar = f.read(1)
	return nextChar

token = ""
while f.read(1):
	f.seek(-1,1)
	c = scanner()
	# print("CHARACTER: " + c)
	if (c != ' ' and c != '\n'):
		token = token + c
		# print(string)
	else:
		lexer(token)
		token = ""

f.close()
