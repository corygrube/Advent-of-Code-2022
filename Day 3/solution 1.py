# Day 3
# Part 1

def get_pri(item_type):
	"""
	Convert item type (ascii letter) to new 1-52 scale.
	a-z = 1-26
	A-Z = 27-52
	
	args:
		item_type (string): single ascii letter representing item type
	
	returns:
		priority (int): equivalent priority for this letter
	"""
	# get ascii code for item type
	ordinal = ord(item_type)
	
	# adjust priority based on whether item type is upper or lower case
	# losercase - 'a' begins at 97, so subtract 96 to get 1-26
	if ordinal > 96:
		return ordinal - 96
	# uppercase - 'A' begins at 65, so (type - 64 + 26) -> (type - 38)
	return ordinal - 38

with open('Day 3\\input.txt', 'r') as file:
	# read as list of lines
	input = file.read().splitlines()
		
	total = 0
	for rucksack in input:
		# separate into two compartments of rucksack
		mid = int(len(rucksack)/2)
		c1 = rucksack[:mid]
		c2 = rucksack[mid:]

		# use set intersection to find matching item type
		match = ''.join(set(c1).intersection(c2))

		# get priority of item type and add to priority total
		total = total + get_pri(match)
	
	print(total)
