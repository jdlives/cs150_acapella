with open('test.txt', 'r') as f:							#file reading
    sourceText = f.read()

#####START OF FUNCTIONS/CLASSES#####

class Character:
	def __init__(self, c, rowIndex, colIndex, sourceIndex, sourceText):	#initialize class
		self.c 			= c
		self.rowIndex 	= rowIndex
		self.colIndex	= colIndex
		self.sourceIndex= sourceIndex
		self.sourceText	= sourceText

	def __str__(self):										#for printing
		if self.c == " ":
			self.c = "   space"
		elif self.c == "\n":
			self.c = "   newline"
		elif self.c == "\t":
			self.c = "   tab"
		elif self.c == "\0":
			self.c = "   eof"
		
		return (
              str(self.rowIndex).rjust(6)
            + str(self.colIndex).rjust(4)
            + "  "
            + self.c
            )
		
def initialize(textArg):									#initialize global variables
	global lastIndex, rowIndex, colIndex, sourceIndex, sourceText
	sourceText	 = textArg
	lastIndex    = len(sourceText) - 1
	sourceIndex  = -1
	rowIndex     =  0
	colIndex     = -1
	
def get():
	global lastIndex, rowIndex, colIndex, sourceIndex, sourceText
	sourceIndex += 1    									# increment the index in sourceText

	# maintain the line count
	if sourceIndex > 0:
		if sourceText[sourceIndex - 1] == "\n":				#new line in text, reset colIndex
			rowIndex += 1
			colIndex  = -1

	colIndex += 1

	if sourceIndex > lastIndex:								#end of file
		char = Character("\0", rowIndex, colIndex, sourceIndex, sourceText)
	else:
		c    = sourceText[sourceIndex]
		char = Character(c, rowIndex, colIndex, sourceIndex, sourceText)

	return char

#####START OF SCRIPT#####
	
print "Here are the characters returned by the scanner:"
print "  line col  character"
initialize(sourceText)
character = get()							#get first
while True:
	print(character)
	if character.c == "   eof": break
	character = get()   					# getnext
