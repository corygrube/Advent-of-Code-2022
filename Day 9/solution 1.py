# Day 9
# Part 1

class Head:
	def __init__(self):
		# position
		self.x = 0
		self.y = 0
		# position history (x, y)
		self.history = [(0,0)]

	def record_history(self):
		"""log current position to history"""
		position = (self.x, self.y)
		self.history.append(position)

class Tail:
	def __init__(self):
		# position
		self.x = 0
		self.y = 0
		# position history (x, y)
		self.history = [(0,0)]
	
	def record_history(self):
		"""log current position to history"""
		position = (self.x, self.y)
		self.history.append(position)
	
	def get_positions(self):
		"""count number of unique positions"""
		history_set = set(self.history)
		return len(history_set)

class Rope:
	def __init__(self):
		# rope has head/tail. tail tracks head.
		self.head = Head()
		self.tail = Tail()
	
	def move(self, direction):
		"""Move head, record position, move tail if required"""
		# move up 1
		if direction == "U":
			self.head.y += 1
		
		# move down 1
		elif direction == "D":
			self.head.y -= 1

		# move left 1
		elif direction == "L":
			self.head.x -= 1
		
		# move right 1
		elif direction == "R":
			self.head.x += 1
		
		# log head position, move tail (if req)
		self.head.record_history()
		self._move_tail()

	
	def _move_tail(self):
		"""move tail if not directly adjacent to head"""
		# calculate x/y differences
		x_dif = self.head.x - self.tail.x
		y_dif = self.head.y - self.tail.y

		# if x is more than 1 forward, move tail x
		if x_dif > 1:
			self.tail.x += 1
			# if y is not zero, indicates head/tail were originally diagonal. Align y.
			if y_dif != 0:
				self.tail.y = self.head.y
		
		# if x is more than 1 back, move tail x
		elif x_dif < -1:
			self.tail.x -= 1
			# if y is not zero, indicates head/tail were originally diagonal. Align y.
			if y_dif != 0:
				self.tail.y = self.head.y
		
		# if y is more than 1 forward, move tail y
		if y_dif > 1:
			self.tail.y += 1
			# if x is not zero, indicates head/tail were originally diagonal. Align x.
			if x_dif != 0:
				self.tail.x = self.head.x
		
		# if y is more than 1 back, move tail y
		elif y_dif < -1:
			self.tail.y -= 1
			# if x is not zero, indicates head/tail were originally diagonal. Align x
			if x_dif != 0:
				self.tail.x = self.head.x

		# record tail position
		self.tail.record_history()


def get_input(path): 
	"""Open prompt file, return as list of lines"""
	with open(path) as file:
		return file.read().splitlines()

# main
commands = get_input('Day 9\\input.txt')

rope = Rope()
for command in commands:
	# spit command into component parts
	direction, distance = command.split(' ')
	distance = int(distance)

	# move {distance} times in given direction 
	for _ in range(distance):
		rope.move(direction)

print(rope.tail.get_positions())