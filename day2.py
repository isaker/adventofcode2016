# --------------------------------------------
# Start of execution
# --------------------------------------------

x = 1
y = 1
code = ""

instructions = file("bathroom_instructions.txt").read().split()

for instr in instructions:
	print instr
	for move in instr:
		#print move
		if move == 'U' and ([x,y] in [[2,1],[1,2],[2,2],[3,2],[1,3],[2,3],[3,3],[2,4]]):
			y -= 1
		elif move == 'D' and ([x,y] in [[2,0],[1,1],[2,1],[3,1],[1,2],[2,2],[3,2],[2,3]]):
			y += 1
		elif move == 'R' and ([x,y] in [[1,1],[2,1],[0,2],[1,2],[2,2],[3,2],[1,3],[2,3]]):
			x += 1
		elif move == 'L' and ([x,y] in [[3,1],[2,1],[4,2],[3,2],[2,2],[1,2],[3,3],[2,3]]):
			x -= 1 

	if [x,y] == [2,0]:
		code = code + '1'
	elif [x,y] == [1,1]:
		code = code + '2'
	elif [x,y] == [2,1]:
		code = code + '3'
	elif [x,y] == [3,1]:
		code = code + '4'
	elif [x,y] == [0,2]:
		code = code + '5'
	elif [x,y] == [1,2]:
		code = code + '6'
	elif [x,y] == [2,2]:
		code = code + '7'
	elif [x,y] == [3,2]:
		code = code + '8'
	elif [x,y] == [4,2]:
		code = code + '9'
	elif [x,y] == [1,3]:
		code = code + 'A'
	elif [x,y] == [2,3]:
		code = code + 'B'
	elif [x,y] == [3,3]:
		code = code + 'C'
	elif [x,y] == [2,4]:
		code = code + 'D'

	print code