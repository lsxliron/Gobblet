from gobblet import *
class Square(object):
	"""
	This class represents a Square on the board
	"""

	def __init__(self):
		self.stack = list()
		for i in range(0,3):
			self.stack.append(Gobblet())

	def __str__(self):
		return str(self.stack)

	def __repr__(self):
		return str(self.stack)

	def full(self):
		for i in range(0,3):
				if self.stack[i].dummy():
					return False
		return True

	def empty(self):
		"""
		Returns true if a square is empty or false otherwise
		"""
		return self.stack[0].dummy()


	



