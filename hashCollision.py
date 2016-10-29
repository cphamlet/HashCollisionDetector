import random, hashlib, string, itertools

#FUNCTIONS
#This function returns a random string with uppercase characters, lowercase characters, and numbers
def randomstring(length):
		#string.lowercase + uppercase and the numbers indicate the character space
   return ''.join(random.choice(string.lowercase+string.uppercase+"0123456789") for i in range(length))
#END FUNCTIONS

#SPECIFIED PARAMETERS
#N stands for the first "N" digits of the hash result, 6*4 bits per hex digit = 24 bits
N = 6
f = open("testResults.txt", 'w')
f.write("These are the results\n\n")
f.close()

#END PARAMETERS


#Holds the total number of computations to crack hash (used for average). Do NOT Change

	#A Hashmap holds our hash values, access time Avg(1) 
mapofHashes = {}
	#get random string
word = randomstring(9)
	
	#This creates a key value pair, with the hash of the random string being the key
	# The value is the random word
mapofHashes[hashlib.md5(bytes(word)).hexdigest()[0:N]] = word
print("Completed hash pre-computation")
	
	#Holds the number of computations to crack hash
hashComputations = 0
	
	#We will break the loop once we find a collision
for guess in itertools.product(string.lowercase+string.uppercase+'0123456789', repeat = 3):
	#Take a string at random, and save the hash
	#Here we bruteforce random strings because bruteforce gives same answer
	joinedGuess = ''.join(guess)
	hashTemp = hashlib.md5(bytes(joinedGuess)).hexdigest()[0:N]
	hashComputations = hashComputations + 1

	#If the hash mataches, and the random word does not equal our existing
	#word, then you have a valid collision
	if (hashTemp in mapofHashes):
		f = open("testResults.txt","a")

		f.write("\n")
		f.write("\nWord1 : " + mapofHashes[hashTemp])
		f.write("\nWord2 : " + joinedGuess)
		f.write("\nHASH: " + hashTemp)
		f.write("\nComputations to find collision: " + str(hashComputations))
		f.close()
	elif len(mapofHashes) < 10000000:
		mapofHashes[hashTemp] = joinedGuess

#Prints stats

#for guess in itertools.product(string.lowercase+string.uppercase+'0123456789', repeat=10):

#if collisionsFound == 1000:
	#	break
	#else:

