import hashlib

def getMD5(myString):
	return hashlib.md5(myString).hexdigest()

def findCoins(magicString, beginningStringToMatch, numberOfCoinsToFind):
	coinsFound = []
	counter = 0
	while (len(coinsFound) < numberOfCoinsToFind):
		tempString = magicString + str(counter)
		myMD5 = getMD5(tempString)
		#print(tempString + " : " + myMD5)
		if (myMD5[0:len(beginningStringToMatch)] == beginningStringToMatch):
			coinsFound.append(tempString)
		counter += 1
	return coinsFound
		
def printCoinList(coinsFound):
	for coin in coinsFound:
		print(coin)
		
# Part 1
magicString = "yzbqklnj"
coins = findCoins(magicString, "00000", 1)
printCoinList(coins)

# Part 2
coins = findCoins(magicString, "000000", 1)
printCoinList(coins)