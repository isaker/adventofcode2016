def is_even(int):
	if (int%2==0):
		return True
	else:
		return False

def even_ones_bit(int):
	binary = bin(int)[2:]
	print binary
	ones = 0
	for char in binary:
		#print "char: " + char
		if char == '1':
			ones += 1
	print "ones: " + str(ones)
	if is_even(ones):
		return True
	else:
		return False

def print_map(map):
	map = [[] for _ in range(size_of_map)]
	for list in map:
		for xlist in list:
			map


# --------------------------------------------
# Start of execution
# --------------------------------------------
size_of_map = 4
fav_number = 4
header = " "
map_list = [[[] for _ in range(size_of_map)] for _ in range(size_of_map)]

for x in range(1,size_of_map):
	map_list[x][0].append(x)
	map_list[0][x].append(x)
print map_list

print header

for x in range(size_of_map):
	for y in range(size_of_map):
		start_number = x * x + 3 * x + 2 * x * y + y + y * y +fav_number
		#print start_number
		#print "even ones: " + str(even_ones_bit(start_number))