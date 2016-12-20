import sys
# --------------------------------------------
# Start of execution
# --------------------------------------------
num_elves = 300529
start_elves = float(num_elves)
elf_presents = []
for i in range(1,num_elves+1):
	elf_presents.append([i,1])

#print elf_presents

i = 0
while len(elf_presents) > 1:
	elf_presents[i][1] += elf_presents[(i+1)%num_elves][1]
	del elf_presents[(i+1)%num_elves]
	num_elves = len(elf_presents)
	num_elvesF = float(len(elf_presents)) 
	if (i+1) > num_elves:
		i=0
	else: 
		i += 1
	percent = (start_elves - num_elves) / start_elves
	text = "\rProgress: " + str(round(percent*100, 2)) + "%"
	sys.stdout.flush()
	sys.stdout.write(text)
	


print "\nlast elf left: "+str(elf_presents)
