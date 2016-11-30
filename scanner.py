import sys
f = open("test.txt", 'r')					#open file
#FUNCTIONS
def getChar():			
		global nextChar
		nextChar = f.read(1)
		if not nextChar:					#c became empty, indicating end
			print "End"


#START OF CODE			
for i in range (1,6):						#checking if getChar() works
	getChar()
	sys.stdout.write("%c" %(nextChar))

f.close()									#close file