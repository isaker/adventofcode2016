import time


def isTrap(tiles):
	if tiles[0] == '^' and tiles[1] == '^' and tiles[2] == '.':
		return True
	elif tiles[0] == '.' and tiles[1] == '^' and tiles[2] == '^':
		return True
	elif tiles[0] == '^' and tiles[1] == '.' and tiles[2] == '.':
		return True
	elif tiles[2] == '^' and tiles[0] == '.' and tiles[1] == '.':
		return True

	return False

def isTrapFirst(tiles):
	if tiles[0] == '^' and tiles[1] == '^':
		return True
	elif tiles[0] == '.' and tiles[1] == '^':
		return True
	return False

def isTrapLast(tiles):
	if tiles[0] == '^' and tiles[1] == '^':
		return True
	elif tiles[0] == '^' and tiles[1] == '.':
		return True
	return False

# --------------------------------------------
# Start of execution
# --------------------------------------------
rows = 400000
lastRow = file("startrow.txt").read()
room = lastRow + '\n'

for i in range(rows-1):
	newRow = ''
	#print "startrow: " + lastRow

	if isTrapFirst(lastRow[0:2]):
		newTile = '^'
	else:
		newTile = '.'

	newRow += newTile

	#print "newrow: " + newRow

	for tile in range(1,len(lastRow)-1):
		#print tile
		#print "lastrow[tile:tile+3]: " + lastRow[tile-1:tile+2]
		if isTrap(lastRow[tile-1:tile+2]):
			newTile = '^'
		else:
			newTile = '.'
		newRow += newTile
		#print newRow
		#print "newtile: " + newTile

	if isTrapLast(lastRow[-2:]):
		newTile = '^'
	else:
		newTile = '.'

	newRow += newTile
	lastRow = newRow
	print newRow

	room += newRow + '\n'

numTraps = room.count('^')
numSafe = room.count('.')

print "trap tiles: " + numTraps
print "safe tiles: " + numSafe

