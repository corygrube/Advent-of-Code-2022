# Day 1

# Part 1
with open('Day 1\\input.txt', 'r') as file:
	# read as list of lines
	lines = file.readlines()
	
	cal = 0
	cal_max = 0
	# iterate through lines (calories)
	for line in lines:
		# remove line breaks. fallback to 0 for empty string
		line = int(line.strip() or 0)
		
		# on line break (start of new elf), reset counters and set new max
		if not line:
			cal = 0
			continue
		
		# add new line to elf's total
		cal = cal + line
		if cal > cal_max:
			cal_max = cal

	print(cal_max)
	