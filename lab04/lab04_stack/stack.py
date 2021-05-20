class Stack:
	values = []

	def __init__(self):
		self.values = []

	def pop(self):
		self.values.pop()

	def push(self, data):
		self.values.append(data)

	