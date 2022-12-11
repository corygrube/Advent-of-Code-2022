# Day 5
# Part 1

def get_input(path): 
	"""Open prompt file, return as list of lines"""
	with open(path) as file:
		return file.read().splitlines()

def move(move_qty, move_from, move_to):
	"""
	Move crates one at a time as specified by instruction set.
	Crates will move from top of one column to the top of another.
	
	args:
		move_qty (int): quantity of crates to be moved
		move_from (int): column to move crates from
		move_to (int): column to move crates to
	
	returns:
		None
	"""
	# move counter
	i = 1

	# loop through move instructions
	while i <= move_qty:
		# get top crate in 'from' column (last char in list)
		moved = crates[move_from][-1]
		# remove top crate from 'from' column
		crates[move_from] = crates[move_from][:-1]
		# add moved crate to 'to' column
		crates[move_to] = crates[move_to] + moved

		# loop until qty satisfied
		i = i + 1

def read_top():
	"""
	Print top line of crates after all moves.

	No args or returns.
	"""
	# result string - top line of crates
	top = ''
	for crate in crates:
		# skip any columns with no crates
		if len(crates[crate]) == 0:
			continue
		# add top crate to resut string
		top = top + crates[crate][-1]
	
	print(top)

# crate setup
## sample
# crates = {
# 	1: 'ZN',
# 	2: 'MCD',
# 	3: 'P'
# }

# input
crates = {
	1: 'HRBDZFLS',
	2: 'TBMZR',
	3: 'ZLCHNS',
	4: 'SCFJ',
	5: 'PGHWRZB',
	6: 'VJZGDNMT',
	7: 'GLNWFSPQ',
	8: 'MZR',
	9: 'MCLGVRT'
}

# main
input = get_input('Day 5\\input.txt')
for line in input:
	# ignore initial stack lines, proceed to move instructions
	if 'move' not in line:
		continue
	
	# split line into move instruction variables
	linesplit = line.split(' ')
	move_qty = int(linesplit[1])
	move_from = int(linesplit[3])
	move_to = int(linesplit[5])

	# perform move
	move(move_qty, move_from, move_to)

# read top line of crates
read_top()
