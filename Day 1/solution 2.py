# Day 1

# Part 2
with open('Day 1\\input 1.txt', 'r') as file:
	# read as list of lines
	lines = file.readlines()
	
	cal_list = []
	cal = 0
	# iterate through lines (calories)
	for line in lines:
		# remove line breaks. fallback to 0 for empty string
		line = int(line.strip() or 0)
		
		# on line break (start of new elf), reset counters and set new max
		if not line:
			cal_list.append(cal)
			cal = 0
			continue
		
		# add new line to elf's total
		cal = cal + line

	# sort list by size (large to small)
	cal_list.sort(reverse=True)
	print(sum(cal_list[:3]))
