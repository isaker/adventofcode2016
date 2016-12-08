
def isABBA(chars):
	abba = chars[0:2]
	if abba[0] != abba[1]:
		#print abba
		#print abba[::-1]
		if abba == chars[2:4][::-1]:
			#print abba + abba[::-1]
			return True
	else:
		return False

def splitMsg(msg):
	split = msg.split(']')
	return (split[0], split[1])

def containsABBA(word_list):
	for word in word_list:
		for x in range(len(word)-3):
			if isABBA(word[x]+word[x+1]+word[x+2]+word[x+3]):
				return True
	return False

# --------------------------------------------
# Start of execution
# --------------------------------------------

ips = file("ipv7.txt").read().split()
num_bracket_words = 0
for ip in ips:
	bracket_words = []
	non_bracket_words = []
	#print ip
	templist = ip.split('[')
	non_bracket_words.append(templist[0])

	for x in range(1,len(templist)):
		msg = splitMsg(templist[x])
		non_bracket_words.append(msg[1])
		bracket_words.append(msg[0])
		#print msg

	#print non_bracket_words
	#print bracket_words

	if containsABBA(bracket_words):
		print "abba inside bracket"
		print bracket_words

	elif containsABBA(non_bracket_words):
		print "abba found!"
		print non_bracket_words
		num_bracket_words += 1



	#print number_brackets
	#print templist
	#print "----------------------------"
	#temp = templist[1].split(']')[0]
	#print temp
	#print "----------------------------"
	#for x in range(len(temp)-3):
	#	if isABBA(temp[x] + temp[x+1] + temp[x+2] + temp[x+3]):
	#		print "abba found"

	#templist = [templist[0]] + templist[1].split(']')
	#for x in range(len(templist[1])-3):
	#	if isABBA(templist[1][x]+templist[1][x+1]+templist[1][x+2]+templist[1][x+3]):
	#		print "not abba"
	#		break
#isABBA("abba")

print num_bracket_words

