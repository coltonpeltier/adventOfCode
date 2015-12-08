def surface_area(l,w,h):
	return 2*l*w + 2*w*h + 2*h*l

def smallest_side_area(l,w,h):
	side1 = l*w
	side2 = w*h
	side3 = h*l
	smallest = side1
	if (side2 < smallest):
		smallest = side2
	if (side3 < smallest):
		smallest = side3
	return smallest

def volume(l,w,h):
	return l*w*h

def bow_length(l,w,h):
	#Find the smallest perimeter
	perim1 = 2*l + 2*w
	perim2 = 2*l + 2*h
	perim3 = 2*w + 2*h
	smallest = perim1
	if (perim2 < smallest):
		smallest = perim2
	if (perim3 < smallest):
		smallest = perim3
	return smallest

f = open('input','r')
total = 0
total_with_bow = 0

def solveString(myString, ribbon=False, debug=False):
	dimensions = myString.split('x')
	l = int(dimensions[0])
	w = int(dimensions[1])
	h = int(dimensions[2])
	if (ribbon == False):
		return surface_area(l,w,h) + smallest_side_area(l,w,h)
	elif (ribbon == True):
		if (debug):
			print("Volume: " + str(volume(l,w,h)))
			print("Bow Length: " + str(bow_length(l,w,h)))
			print("Surface Area: " + str(surface_area(l,w,h)))
			print("Smallest Side Area: " + str(smallest_side_area(l,w,h)))
		return volume(l,w,h) + bow_length(l,w,h)

def solvePuzzle(total,total_with_bow):
	for line in f:
		total = total + solveString(line)
		total_with_bow = total_with_bow + solveString(line,True)
		
	print("Total wrapping paper needed: " + str(total))
	print("Total wrapping paper needed for bows: " + str(total_with_bow))

solvePuzzle(total,total_with_bow)

#def debug():
#	unitTests = []
#	unitTests.append("2x3x4")
#	unitTests.append("1x1x10")
#	for test in unitTests:
#		print(test)
#		print(str(solveString(test,True,True)))
#
#debug()