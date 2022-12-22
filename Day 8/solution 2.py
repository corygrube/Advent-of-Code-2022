# Day 8
# Part 2

def get_input(path): 
	"""Open prompt file, return as list of lines"""
	with open(path) as file:
		return file.read().splitlines()	

def get_height(x, y):
	"""get tree height at given coordinates"""
	return trees[x][y]

def get_distance(height, trees):
	"""get viewing distance for a given list of trees"""
	distance = 0
	# print(f'Height {height}, tree test {trees}')
	# distance increases for each tree you can see over (min of 1)
	for tree in trees:
		distance = distance + 1
		if tree >= height:
			break
	
	return distance

def get_distance_left(x, y):
	"""get view distance to left of current tree"""
	height = get_height(x, y)
	# create list jof trees left of current tree
	left_trees = [trees[x][z] for z in range(0,y)]
	left_trees.reverse()
	
	return get_distance(height, left_trees)

def get_distance_right(x, y):
	"""get view distance to right of current tree"""
	height = get_height(x, y)
	# create list jof trees right of current tree
	y_max = len(trees[x])
	right_trees = [trees[x][z] for z in range(y+1,y_max)]
	
	return get_distance(height, right_trees)

def get_distance_up(x, y):
	"""get view distance up from current tree"""
	height = get_height(x, y)
	# create list jof trees up from current tree
	up_trees = [trees[z][y] for z in range(0,x)]
	up_trees.reverse()

	return get_distance(height, up_trees)

def get_distance_down(x, y):
	"""get view distance down from current tree"""
	height = get_height(x, y)
	# create list jof trees down from current tree
	x_max = len(trees)
	down_trees = [trees[z][y] for z in range(x+1,x_max)]

	return get_distance(height, down_trees)

# main
input = get_input('Day 8\\input.txt')

# create 2d array of trees, cast to integer
trees = []
for row in input:
	trees.append([int(x) for x in row])

# iterate through trees find highest score
score_max = 0
for x, row in enumerate(trees):
	# first row has score of 0
	if x == 0:
		continue

	# last row has score of 0
	if x == len(trees) - 1:
		continue

	# iterate through trees in row
	for y, tree in enumerate(row):
		distances = []
		
		# first column has score of 0
		if y == 0:
			continue
		
		# last column has score of 0
		if y == len(row) - 1:
			continue
		
		# get up/down/left/right visibility distance
		distances.append(get_distance_left(x, y))
		distances.append(get_distance_right(x, y))
		distances.append(get_distance_up(x, y))
		distances.append(get_distance_down(x, y))
		
		# print(f'Row {x}, Col {y}, Distances {distances}')
		# calculate score based on view 
		score = 1
		for i in distances:
			score = score * i
		
		# record if new max score
		if score > score_max:
			score_max = score
		
print(score_max)
