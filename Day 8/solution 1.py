# Day 8
# Part 1

def get_input(path): 
	"""Open prompt file, return as list of lines"""
	with open(path) as file:
		return file.read().splitlines()	

def get_height(x, y):
	return trees[x][y]

def is_vis_left(x, y):
	height = get_height(x, y)
	left_trees = [trees[x][z] for z in range(0,y)]
	return height > max(left_trees)

def is_vis_right(x, y):
	height = get_height(x, y)
	y_max = len(trees[x])
	right_trees = [trees[x][z] for z in range(y+1,y_max)]
	return height > max(right_trees)

def is_vis_up(x, y):
	height = get_height(x, y)
	up_trees = [trees[z][y] for z in range(0,x)]
	return height > max(up_trees)

def is_vis_down(x, y):
	height = get_height(x, y)
	x_max = len(trees)
	down_trees = [trees[z][y] for z in range(x+1,x_max)]
	return height > max(down_trees)

# main
input = get_input('Day 8\\input.txt')

# create 2d array of trees, cast to integer
trees = []
for row in input:
	trees.append([int(x) for x in row])

# iterate through trees to count visible
visible = 0
for x, row in enumerate(trees):
	# first row is all visible
	if x == 0:
		visible = visible + len(row)
		continue

	# last row is all visible
	if x == len(trees) - 1:
		visible = visible + len(row)
		continue

	for y, tree in enumerate(row):
		# first column is all visible
		if y == 0:
			visible = visible + 1
			continue
		
		# last column is all visibile
		if y == len(row) - 1:
			visible = visible + 1
			continue

		# check up/down/left/right visibility. Increment if visible from any direction
		if is_vis_left(x, y):
			visible = visible + 1
			continue
		if is_vis_right(x, y):
			visible = visible + 1
			continue
		if is_vis_up(x, y):
			visible = visible + 1
			continue
		if is_vis_down(x, y):
			visible = visible + 1

print(visible)
