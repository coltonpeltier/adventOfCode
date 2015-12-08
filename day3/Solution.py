# Define all possile moves
moves = {}
moves['<'] = "-1,x"
moves['>'] = "1,x"
moves['^'] = "1,y"
moves['v'] = "-1,y"
moves['\n'] = "0,x"
#Make a list for the houses visited
housesVisited = []
housesVisited.append("0,0")

def makeMove(person,move):
	myMove = moves[move].split(',')
	count = int(myMove[0])
	direction = myMove[1]
	person[direction] += count
	coords = str(person['x']) + "," + str(person['y'])
	if (coords not in housesVisited):
		housesVisited.append(coords)

def initializePerson(x=0,y=0):
	newPerson = {}
	newPerson['x'] = x
	newPerson['y'] = y
	return newPerson

# The first case where just santa is following directions
santa = initializePerson()
myInput = open('Input','r')
myChars = myInput.read()
myInput.close()
for char in myChars:
	makeMove(santa,char)
print("Total houses visited (Just Santa): " + str(len(housesVisited)))


#Make a list for the houses visited
housesVisited = []
housesVisited.append("0,0")
santa = initializePerson()
robo = initializePerson()

# The second case where santa and a robot are following directions
santaTurn = True
for char in myChars:
	if (santaTurn):
		makeMove(santa,char)
		santaTurn = False
	else:
		makeMove(robo,char)
		santaTurn = True
print("Total houses visited (Santa +  RoboSanta): " + str(len(housesVisited)))