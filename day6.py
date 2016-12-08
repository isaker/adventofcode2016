import operator

# --------------------------------------------
# Start of execution
# --------------------------------------------

messages = file("messages.txt").read().split()
chars = [[] for lists in range(8)]

for msg in messages:
	for char in range(len(msg)):
		chars[char].append(msg[char])

maxword = ""
minword = ""

for x in range(8):
	alphabet = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
	print "column: " + str(x+1)
	for char in chars[x]:
		alphabet[char] += 1
		print char + ", " + str(alphabet[char])
		
	print alphabet
	maxword = maxword + max(alphabet.iteritems(), key=operator.itemgetter(1))[0]
	minword = minword + min(alphabet.iteritems(), key=operator.itemgetter(1))[0]

#print  char + ", " + str(alphabet[char])
print "maxword: " + maxword
print "minword: " + minword