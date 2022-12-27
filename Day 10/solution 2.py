# Day 10
# Part 2

class Device:
	x = 1			# sprite middle position (length of 3)
	cycle = 1		# CPU cycle
	_row = []		# pixel row
	_screen = []	# screen/pixel output
	
	def _cycle(self, v=None):
		"""
		Generic cycle function

		Increment cycle, add v to x register if given.
		"""
		# draw pixel
		self._draw_pixel()

		# increment cycle
		self.cycle = self.cycle + 1
		
		# move sprite register, if given
		if v:
			self.x = self.x + v
	
	def _draw_pixel(self):
		"""	Draw pixel if sprite is in currently-rendering pixel"""
		# row has 40 pixels
		pixel = len(self._row)
		
		# sprite is 3 px wide. Check if current pixel is occupied by sprite
		if self.x - 1 <= pixel <= self.x + 1:
			# occupied by sprite
			self._row.append('#')
		else:
			# not occupied
			self._row.append('.')
		
		# at end of each pixel row, collapse pixel list to string and add line break
		if len(self._row) == 40:
			self._row.append('\n')
			self._screen.append(''.join(self._row))
			# clear row
			self._row = []

	def addx(self, v):
		"""addx takes two cycles, the second of which adds v to x register."""
		self._cycle()
		self._cycle(v)
	
	def noop(self):
		"""take cycle without modifying x register."""
		self._cycle()
	
	def print_scrn(self):
		"""print screen list as single string"""
		print(''.join(self._screen))

def get_input(path): 
	"""Open prompt file, return as list of lines"""
	with open(path) as file:
		return file.read().splitlines()

# main
input = get_input('Day 10\\input.txt')

# instantiate device
device = Device()

# iterate through commands
for row in input:
	# noop commands
	if 'noop' in row:
		device.noop()
		continue

	# addx command. extract v from command
	v = int(row.split(' ')[1])
	device.addx(v)

device.print_scrn()
