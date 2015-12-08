f = open('input','r')
myData = f.read()
possibilities = {}
possibilities['('] = 1
possibilities[')'] = -1
possibilities['\n'] = 0
floor = 0

for myChar in myData:
	floor += possibilities[myChar]

print(floor)	
