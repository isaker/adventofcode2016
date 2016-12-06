# --------------------------------------------
# Start of execution
# --------------------------------------------

rooms = file("rooms.txt").read().split()

sector_IDs = 0

for room in rooms:
	wroom = room.split('-')
	print wroom
	chars = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0
					,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0
					,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0
					,"v":0,"w":0,"x":0,"y":0,"z":0}
	#print wroom[3]
	for x in range(len(wroom)-1):
		for char in wroom[x]:
			chars[char] += 1

	#print chars
	import operator 
	#sorted_chars = sorted(sorted(chars.items(), key = lambda x : x[1],reverse=True), key = lambda x : x[0])
	sorted_chars = sorted(chars.items(), key = lambda x : (-x[1],x[0]))
	print sorted_chars

	cs = wroom[len(wroom)-1].split('[')

	sect_ID = int(cs[0])

	check_sum = cs[1][0:-1]

	print "check_sum: " + check_sum

	check_check = ""
	for y in range(5):
		check_check = check_check + sorted_chars[y][0]

	print check_check

	if check_check == check_sum:
		sector_IDs += sect_ID

	print sector_IDs

	
