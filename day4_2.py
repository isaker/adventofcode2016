# --------------------------------------------
# Start of execution
# --------------------------------------------

rooms = file("rooms.txt").read().split()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

deciphered_rooms = []

sector_IDs = 0

for room in rooms:
	decoded_name = ""

	wroom = room.split('-')
	#print wroom

	cs = wroom[len(wroom)-1].split('[')
	sect_ID = int(cs[0])
	shift = sect_ID % 26

	words_in_room = []

	for x in range(len(wroom)-1):
		#print wroom[x]
		word = ""
		for char in wroom[x]:
			#print char
			startval = alphabet.index(char)
			newchar = alphabet[(startval + shift) % 26]
			word = word + newchar

		words_in_room.append(word)

	if 'northpole' in words_in_room:
		print "found the north pole"
		northpole_sector = sect_ID

	deciphered_rooms.append(words_in_room)

sorted_dec_rooms = sorted(deciphered_rooms, key = lambda x : x[0])
#print sorted_dec_rooms
print northpole_sector


#%26

