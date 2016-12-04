def isValid(tri):
	a = int(tri[0])
	b = int(tri[1])
	c = int(tri[2])
	if ((a+b)>c and (a+c)>b and (b+c)>a):
		return True
	else:
		return False

# --------------------------------------------
# Start of execution
# --------------------------------------------

valid_triangles = 0
t1 = []
t2 = []
t3 = []

triangles = file("triangles.txt").read().split('\n')
for triangle in triangles:
	t = triangle.split()
	t1.append(t[0])
	t2.append(t[1])
	t3.append(t[2])

#print t1
#print t2
#print t3
	#if (isValid(t)):
		#print str(a) + " + " + str(b) + " = " + str(a+b) + " | c = " + str(c)
		#print "not valid: " + str(t)
	#	valid_triangles += 1
for t in range(0,len(t1)-1,3):
	print [t1[t], t1[t+1], t1[t+2]]
	if isValid([t1[t], t1[t+1], t1[t+2]]):
		valid_triangles += 1

for t in range(0,len(t2)-1,3):
	if isValid([t2[t], t2[t+1], t2[t+2]]):
		valid_triangles += 1

for t in range(0,len(t3)-1,3):
	if isValid([t3[t], t3[t+1], t3[t+2]]):
		valid_triangles += 1

print "valid_triangles: " + str(valid_triangles)

