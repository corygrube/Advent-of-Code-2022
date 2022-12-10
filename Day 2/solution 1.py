# Day 2
# Part 1

def rps(opp_throw, your_throw):
	"""
	Determine winner of a rock paper scissors (rps) match. 
	Returns points earned.
	args:
		opp_throw (string) A/B/C (rock/paper/scissors) for opponent
		your_throw: (string) X/Y/Z (rock/paper/scissors) for player
	
	returns:
		(int) Points won by player
	"""
	score = 0
	# you throw Rock
	if your_throw == 'X':
		score = 1
		# draw
		if opp_throw == 'A':
			score = draw(score)
		# win
		elif opp_throw == 'C':
			score = win(score)

	# you throw Paper
	elif your_throw == 'Y':
		score = 2
		# win
		if opp_throw == 'A':
			score = win(score)
		# draw
		elif opp_throw == 'B':
			score = draw(score)
		
	
	# you throw Scissors
	elif your_throw == 'Z':
		score = 3
		# win
		if opp_throw == 'B':
			score = win(score)
		# draw
		elif opp_throw == 'C':
			score = draw(score)
	
	return score

def draw(score):
	"""increase score by 3 for draw"""
	return score + 3

def win(score):
	"""increase score by 6 for win"""
	return score + 6

with open('Day 2\\input 1.txt', 'r') as file:
	# read as list of lines
	lines = file.readlines()
	# A/X = Rock = 1
	# B/Y = Paper = 2
	# C/Z = Scissors = 3

	score = 0
	for line in lines:
		opp_throw, your_throw = line.strip().split(' ')
		round = rps(opp_throw, your_throw)
		score = score + round
	
	print(score)
	