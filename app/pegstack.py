"""
This class represents an external gobblet stack. This is the stack of
gobblets that the player can put on the board.
This stack does not include the gobblets which are already on the board.
"""
from gobblet import *

class PegStack(object):
	def __init__(self, big_peg, medium_peg, small_peg, tiny_peg):
		"""
		Initializer
		"""
		self.stack=list()
		self.stack.append(tiny_peg)
		self.stack.append(small_peg)
		self.stack.append(medium_peg)
		self.stack.append(big_peg)

	def __str__(self):
		"""
		Prints the stack to the display
		"""
		s = ""
		for i in range(0, len(self.stack)):
			s = s + str(self.stack[i]) + "\n"
		return s

	def __iter__(self):
		for peg in self.stack:
			yield peg

	def pop(self):
		"""
		Pops the top gobblet from the stack
		"""
		return self.stack.pop()

	def top(self):
		"""
		Return the top gobblet in the stack
		"""
		return self.stack[len(self.stack)-1]


	def get_top_size(self):
		"""
		Returns the size of the top gobblet in the stack
		"""
		return self.stack[len(self.stack)-1].size
