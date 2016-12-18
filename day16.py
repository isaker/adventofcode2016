
def calcCheckSum(data):
	checkSum = ''
	for i in range(0,len(data)-1,2):
		if data[i] == data[i+1]:
			checkSum += '1'
		else:
			checkSum += '0'

	return checkSum

# --------------------------------------------
# Start of execution
# --------------------------------------------
disksize = 35651584
a = lastRow = file("initdragoncurve.txt").read()

while len(a) < disksize:
	b = a[::-1]
	newb = ''
	for char in b:
		if char == '1':
			newb += '0'
		else: 
			newb += '1'
	a = a + '0' + newb
	print a


a = a[0:disksize]

cSum = calcCheckSum(a)
while(len(cSum) % 2 == 0):
	print cSum
	cSum = calcCheckSum(cSum)
print "checksum: " + cSum