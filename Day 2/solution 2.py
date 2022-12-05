# Day 2
# Part 2

def rps(opp_throw, outcome):
	"""
	Determine winner of a rock paper scissors (rps) match. 
	Returns points earned.
	args:
		opp_throw (string) A/B/C (rock/paper/scissors) for opponent
		outcome: (string) X/Y/Z (lose/draw/win) for player
	
	returns:
		(int) Points won by player
	"""
	your_throw = ''
	# get your throw based on opp throw and outcome
	# loss required
	if outcome == 'X':
		if opp_throw == 'A':
			your_throw = 'C'
		elif opp_throw == 'B':
			your_throw = 'A'
		elif opp_throw == 'C':
			your_throw = 'B'

	# draw required
	elif outcome == 'Y':
		your_throw = opp_throw

	# win required
	elif outcome == 'Z':
		if opp_throw == 'A':
			your_throw = 'B'
		elif opp_throw == 'B':
			your_throw = 'C'
		elif opp_throw == 'C':
			your_throw = 'A'
	
	# use a scoring dictionary to determine score for round
	scoring = {
		'A': 1,
		'B': 2,
		'C': 3,
		'X': 0,
		'Y': 3,
		'Z': 6
	}
	return scoring[your_throw] + scoring[outcome]

with open('Day 2\\input 1.txt', 'r') as file:
	# read as list of lines
	lines = file.readlines()
	# A = opp Rock, B = opp Paper, C = opp Scissors
	# X = Lose, Y = Draw, Z = Win

	score = 0
	for line in lines:
		opp_throw, outcome = line.strip().split(' ')
		round = rps(opp_throw, outcome)
		score = score + round
	
	print(score)
