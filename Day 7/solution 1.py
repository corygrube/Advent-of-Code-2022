# Day 7
# Part 1

class Directory:
	size = 0
	contents = []

	def __init__(self, name, ptr=1):
		"""initialize with directory name"""
		self.name = name
		self.ptr = ptr

		# Browse through directory until '$ cd ..' or end of puzzle input
		while self.ptr < len(rows):
			print(f'Pointer: {self.ptr}')
			# current row
			row = rows[self.ptr]

			# file rows start with digit
			if row[0].isdigit():
				file_size, file_name = row.split(' ')
				print(f'Adding file: {file_name}, {file_size}')
				self.add_file(file_name, file_size)
				self.increment_ptr()
				continue

			# step out of dir - directory ends
			if row == '$ cd ..':
				print(f'Leaving dir: {self.name}')
				return
			
			# remaining cd rows are new directories
			if '$ cd ' in row:
				# recursively create new dir (returns final ptr)
				dir_name = row.split(' ')[2]
				print(f'Adding dir: {dir_name}')
				self.ptr = self.add_dir(dir_name, self.ptr+1)
				print(f'Current dir: {self.name}. Finished pointer: {self.ptr}')

				# increment ptr
				self.increment_ptr()
				continue
			
			print(f'No action - incrementing ptr')
			self.increment_ptr()
	
	def get_size(self):
		"""returns current directory size"""
		return self.size
	
	def add_file(self, name, size):
		"""create file, add to dir, add size to directory total"""
		new_file = File(name, int(size))
		self.contents.append(new_file)
		self.size = self.size + new_file.get_size()
		print(f'File added: {name}, {new_file.get_size()}')

	def add_dir(self, name, ptr):
		"""create dir, add to current dir, add size to directory total"""
		new_dir = Directory(name, ptr)
		self.contents.append(new_dir)
		new_dir_size = new_dir.get_size()
		self.size = self.size + new_dir_size
		print(f'Directory added: {name}, {new_dir_size}')

		# sum any directory whose size is below DIR_MAX
		DIR_MAX = 100000
		global dir_sum
		if new_dir_size < DIR_MAX:
			dir_sum = dir_sum + new_dir_size
		
		# returns final ptr for recursion
		return new_dir.get_ptr()
	
	def increment_ptr(self):
		"""increment pointer by 1"""
		self.ptr = self.ptr + 1
	
	def get_ptr(self):
		"""return pointer value"""
		return self.ptr


class File:
	def __init__(self, name, size):
		"""initialize with name and disk size"""
		self.name = name
		self.size = size
	
	def get_size(self):
		"""returns current file size"""
		return self.size


def get_input(path): 
	"""Open prompt file, return as list of lines"""
	with open(path) as file:
		return file.read().splitlines()	

# main
rows = get_input('Day 7\\input.txt')

# build directory, print sum of directories less than 100000 in size
dir_sum = 0
root = Directory('/')
print(dir_sum)