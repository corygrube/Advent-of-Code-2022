# Day 6
# Part 1
from collections import Counter

def get_input(path): 
	"""Open prompt file, return as string"""
	with open(path) as file:
		return file.read()

def is_unique(test):
	"""
	Check if string contains all unique characters

	args:
		test (string): string of any length
	
	returns:
		true (unique) / false (not unique)
	"""
	unique_len = len(Counter(test))
	if unique_len == len(test):
		return True
	return False

# main
input = get_input('Day 6\\input.txt')

test = ''
# iterate through string
for i, char in enumerate(input):
	# add next character
	test = test + char

	# don't check uniqueness if test length is not valid
	if len(test) < 4:
		continue

	# strip first char if more than 4
	if len(test) > 4:
		test = test[1:5]
	
	# check uniqueness
	if is_unique(test):
		# if unique, print unique sequence and character number (offset by 1)
		print(test)
		print(i+1)
		break
