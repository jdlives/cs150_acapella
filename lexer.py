import sys

filename = "test.txt"
f = open("test.txt", 'r')

def lexer(string):

	print(string)

	keywords = "play pause stop repeat chorus duet solo cue final prelude postlude interlude"
	keyword = keywords.split()

	oneCharSymbols = "= ( ) [ ] rewind forward + - * / % ! duet solo > < ,"
	symbol1 = oneCharSymbols.split()

	twoCharSymbols = "== != >= <= += -= *= /="
	symbol2 = twoCharSymbols.split()

	identifiers = "Do Re Mi Fa So La Ti lyrics verse album albums symphony symphonies playlist"
	identifier = identifiers.split()

	for i in range(0,len(keyword)):
		if string == keyword[i]:
			print("KEYWORD")

	for i in range(0, len(symbol1)):
		if string == symbol1[i]:
			print("ONE-CHAR OPERATOR")

	for i in range(0, len(symbol2)):
		if string == symbol2[i]:
			print("TWO-CHAR OPERATOR")

	for i in range(0, len(identifier)):
		if string == identifier[i]:
			print("IDENTIFIER")


def scanner():
	global nextChar
	nextChar = f.read(1)
	return nextChar

string = ""
while f.read(1):
	f.seek(-1,1)
	c = scanner()
	# print("CHARACTER: " + c)
	if (c != ' ' and c != '\n'):
		string = string + c
		# print(string)
	else:
		lexer(string)
		string = ""

f.close()
