import sys

# --------------------------------------------
# Start of execution
# --------------------------------------------
blockedips = file("blockedips.txt").read().split()
#print blockedips
blockedips = sorted(blockedips)
#print blockedips

newblockedips = []

lowestip = 0

i = 0
for iprange in blockedips:
	hilo = iprange.split('-')
	lo = int(hilo[0])
	hi = int(hilo[1])
	newblockedips.append([lo, hi])

newblockedips = sorted(newblockedips)

for iprange in newblockedips:
	lo = iprange[0]
	hi = iprange[1]
	if lo <= lowestip and lowestip <= hi and lowesthi < hi:
		lowestip = hi + 1
		lowesthi = hi
	i += 1
	percent = i/1176
	text = "\rProgress: " + str(round(percent*100, 2)) + "%"
	sys.stdout.flush()
	sys.stdout.write(text)

#print newblockedips

print "\nlowest avaialable ip address: " + str(lowestip)
