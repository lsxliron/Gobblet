

class Gobblet(object):

	def __init__(self, color= -1, size = -1, copy=None):
		if not copy:
			self.color = color
			self.size = size
		else:
			#Copy constructor
			self.color = copy.color
			self.size = copy.size

	def __str__(self):
		return "(color: {c}, size: {s})".format(c=self.color, s=self.size)

	def __repr__(self):
		if self.color == -1 and self.size == -1:
			return "(free)"
		else:
			return "(color: {c}, size: {s})".format(c=self.color, s=self.size)

	def dummy(self):
		"""
		Returns true when a gobblet is dummy (size -1 and color -1)
		or false otherwise
		"""
		if self.color == -1 and self.size == -1:
			return True
		return False

