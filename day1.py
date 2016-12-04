class Direction:
# north = 0
# east = 1 
# south = 2
# west = 3
	def __init__(self):
		self.direction = 0

	def turnLeft(self):
		self.direction = (self.direction - 1) % 4

	def turnRight(self):
		self.direction = (self.direction + 1) % 4

	def getDir():
		return direction

	def printDir(self):
		if self.direction == 0:
			print "facing NORTH"
		elif self.direction == 1:
			print "facing EAST"
		elif self.direction == 2:
			print "facing SOUTH"
		elif self.direction == 3:
			print "facing WEST"

# --------------------------------------------
# Start of the program
# --------------------------------------------

dir = Direction()
dir.printDir()
found_first_double = False
x = 0
y = 0
history = []
commands = file("commands.txt").read().split(', ')
for cmd in commands:
	temp_history = []
	#if found_first_double == False:
	#	print [x,y]
	#	print history
	#	if [x,y] in history:
	#		first_double = abs(x) + abs(y)
	#		found_first_double = True

	#print cmd
	if cmd[0] == 'R':
		dir.turnRight()
	elif cmd[0] == 'L':
		dir.turnLeft()
	if dir.direction == 0:
		for y_prime in range (1, int(cmd[1:])+1):
			if found_first_double == False:
				print [x,y+y_prime]
				print history
				if [x,y+y_prime] in history:
					first_double = abs(x) + abs(y+y_prime)
					found_first_double = True
			history.append([x,y+y_prime])
		y += int(cmd[1:])
	elif dir.direction == 2:
		for y_prime in range (1, int(cmd[1:])+1):
			if found_first_double == False:
				print [x,y-y_prime]
				print history
				if [x,y-y_prime] in history:
					first_double = abs(x) + abs(y-y_prime)
					found_first_double = True
			history.append([x,y-y_prime])
		y -= int(cmd[1:])
	elif dir.direction == 1:
		for x_prime in range (1, int(cmd[1:])+1):
			if found_first_double == False:
				print [x+x_prime,y]
				print history
				if [x+x_prime,y] in history:
					first_double = abs(x+x_prime) + abs(y)
					found_first_double = True
			history.append([x+x_prime,y])
		x += int(cmd[1:])
	elif dir.direction == 3:
		for x_prime in range (1, int(cmd[1:])+1):
			if found_first_double == False:
				print [x-x_prime,y]
				print history
				if [x-x_prime,y] in history:

					first_double = abs(x-x_prime) + abs(y)
					found_first_double = True
			history.append([x-x_prime,y])
		x -= int(cmd[1:])

	dir.printDir()
	
	#print history

		#for place in history:
		#	if place[0] == x and place[1] == y:
		#		first_double = abs(x) + abs(y)
		#		found_first_double = True

dis = abs(x)+abs(y)
print "Distance: " + str(dis)
if found_first_double:
	print "Distance to first visited twice: " + str(first_double)