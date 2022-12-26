# Day 10
# Part 1

class Device:
	x = 1
	cycle = 1
	signal = 0
	_signal_cycles = [20, 60, 100, 140, 180, 220]
	
	def _add_cycle(self, v=None):
		"""
		Generic add cycle function

		Increment cycle, add v to x register if given.
		Checks if cycle is one of the special 'signal' cycles and add signal accordingly.
		"""
		self.cycle = self.cycle + 1
		if v:
			self.x = self.x + v
			print(f'Addx: Adding {v}. Total: {self.x}')
		print(f'Cycle is {self.cycle}')
		if self.cycle in self._signal_cycles:
			self._add_signal()
	
	def _add_signal(self):
		"""Special signal cycles calculate a partial signal based on cycle and add to total."""
		signal_partial = self.cycle * self.x
		print(f'Adding partial signal: {signal_partial}')
		self.signal = self.signal + signal_partial

	def addx(self, v):
		"""addx takes two cycles, the second of which adds v to x register."""
		self._add_cycle()
		self._add_cycle(v)
	
	def noop(self):
		"""Increments cycle without modifying x register."""
		self._add_cycle()
	
	def get_signal(self):
		return self.signal

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

print(device.signal)
