def intialize_light_array(xSize=1000,ySize=1000):
	lightArray = {}
	seperator = ','
	for x in range(0,xSize):
		for y in range(0,ySize):
			lightArray[str(x) +  seperator + str(y)] = False
	return lightArray

def execute_command(commandLine, lightArray):
	if ("toggle" in commandLine):
		execute_toggle(commandLine, lightArray)
	elif ("turn on" in commandLine):
		execute_turn_on(commandLine, lightArray)
	elif ("turn off" in commandLine):
		execute_turn_off(commandLine, lightArray)

def execute_toggle(commandLine, lightArray):
	arrayAffected = find_affected_array(commandLine)
	for point in arrayAffected:
		if (lightArray[point] == True):
			lightArray[point] = False
		else:
			lightArray[point] = True

def execute_turn_on(commandLine, lightArray):
	arrayAffected = find_affected_array(commandLine)
	for point in arrayAffected:
		lightArray[point] = True

def execute_turn_off(commandLine, lightArray):
	arrayAffected = find_affected_array(commandLine)
	for point in arrayAffected:
		lightArray[point] = False

def find_affected_array(commandLine):
	possibleStartingNumbers = "0123456789"
	lowestIndex = 999
	for number in possibleStartingNumbers:
		firstIndex = commandLine.find(number)
		if (firstIndex < lowestIndex and firstIndex != -1):
			lowestIndex = firstIndex
	importantPart = commandLine[lowestIndex:]
	splitItUp = importantPart.split(' ')
	
	topLeft = splitItUp[0]
	bottomRight = splitItUp[2]
	xTop = topLeft.split(',')[0]
	yTop = topLeft.split(',')[1]
	xBottom = bottomRight.split(',')[0]
	yBottom = bottomRight.split(',')[1]
	
	affectedArray = []
	
	for x in range(int(xTop),int(xBottom)+1):
		for y in range(int(yTop),int(yBottom)+1):
			affectedArray.append(str(x) + ',' + str(y))
	
	return affectedArray

myLights = intialize_light_array()
f = open('myData.dat','r')
for line in f:
	execute_command(line,myLights)

lightsOn = 0
for light in myLights:
	if (myLights[light] == True):
		lightsOn += 1

print("There are " + str(lightsOn) + " lights on!")
