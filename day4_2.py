# --------------------------------------------
# Start of execution
# --------------------------------------------

rooms = file("rooms.txt").read().split()

sector_IDs = 0
valid_rooms = []

for room in rooms:
	wroom = room.split('-')
	if len(wroom) == 4:
		if len(wroom[0]) == 5 and len(wroom[1]) == 4: #and len(wroom[2]) == 7:
			valid_rooms.append(wroom)
			print wroom

			cs = wroom[len(wroom)-1].split('[')

			sect_ID = int(cs[0])

			cipher = sect_ID % 26
			print cipher
#%26

