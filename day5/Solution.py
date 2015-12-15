def check_at_least_three_vowels(myString):
	vowels = 0
	vowels += countLetterFrequency(myString, 'a')
	vowels += countLetterFrequency(myString, 'e')
	vowels += countLetterFrequency(myString, 'i')
	vowels += countLetterFrequency(myString, 'o')
	vowels += countLetterFrequency(myString, 'u')
	if (vowels >= 3):
		return True
	else:
		return False
	
def countLetterFrequency(myString, letter):
	splitted = myString.split(letter)
	return len(splitted) - 1

def check_double_letter(myString):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for letter in alphabet:
		doubleLetter = letter + letter
		if (doubleLetter in myString):
			return True
	return False
	
def contains_nefarious_sequence(nefSequenceList, myString):
	for seq in nefSequenceList:
		if (seq in myString):
			return True
	return False

def is_nice_string(myString, nefSequenceList):
	vowelPass = check_at_least_three_vowels(myString)
	doubleLetters = check_double_letter(myString)
	nefarious = contains_nefarious_sequence(nefSequenceList, myString)
	if (vowelPass == True and doubleLetters == True and not nefarious):
		return True
	else:
		return False

def two_letter_repeats(myString):
	# This is for part 2
	if (len(myString) < 4):
		return False
	# Initialize string pointer at 2, since we want two consec
	# utive letters
	pointer = 2
	while (pointer < len(myString) + 1):
		substr = myString[pointer - 2:pointer]
		if (substr in myString[pointer:]):
			return True
		pointer += 1
	return False

def check_one_between(myString):
	#This is for part 2
	# This will take at least 3 letters to be possible
	if (len(myString) < 3):
		return False
	# Initialize pointer at 3
	pointer = 3
	while (pointer < len(myString) + 1):
		substr = myString[pointer - 3: pointer]
		if (substr[0] == substr[2]):
			return True
		pointer += 1
	return False
		
nefariousSequences = ["ab", "cd", "pq", "xy"]

# Part 1
niceStrings = 0
f = open('Input.dat','r')
for line in f:
	isNice = is_nice_string(line, nefariousSequences)
	if (isNice):
		niceStrings += 1
print("Nice strings in Input file (Part 1): " + str(niceStrings))
f.close()

# Part 2
niceStrings = 0
f = open('Input.dat','r')
for line in f:
	if (two_letter_repeats(line) and check_one_between(line)):
		niceStrings += 1
print("Nice strings in Input file (Part 2): " + str(niceStrings))
f.close()

