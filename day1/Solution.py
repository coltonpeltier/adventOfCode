f = open('input','r')
myData = f.read()
possibilities = {}
possibilities['('] = 1
possibilities[')'] = -1
possibilities['\n'] = 0
floor = 0
count = 0
hasEnteredBasement = False

for myChar in myData:
	count += 1
	floor += possibilities[myChar]
	if (floor == -1 and hasEnteredBasement == False):
		print("First entered basement at position " + str(count))
		hasEnteredBasement = True

print(floor)	
