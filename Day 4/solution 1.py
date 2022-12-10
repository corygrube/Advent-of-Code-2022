# Day 4
# Part 1

def get_input(path): 
	"""Open prompt file, return as list of lines"""
	with open(path) as file:
		return file.read().splitlines()

def get_set(id_range):
	"""
	Given a range string, return a set

	args:
		id_range (string): integer range, fmt: '5-7' (low-high)
	
	returns:
		set with all numbers in range
	"""
	# split and typecast to int
	id_range = id_range.split('-')
	low = int(id_range[0])
	high = int(id_range[1])

	# some entries have range of 1 - create set of 1 by hand
	if low == high:
		return {int(low)}
	# otherwise return set via range()
	return set(range(int(low), int(high)+1))

# main
input = get_input('Day 4\\input.txt')

subsets = 0
# split each line into pair of ID ranges
for pair in input:
	range1, range2 = pair.split(',')
	
	# get set for each ID range
	set1 = get_set(range1)
	set2 = get_set(range2)

	# increment subsets if either set contains the other
	if set1.issubset(set2) or set1.issuperset(set2):
		subsets = subsets + 1

print(subsets)
