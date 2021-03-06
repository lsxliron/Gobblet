"""
This class represents a state of the game
"""


class Node(object):
	def __init__(self, board_state, hv, peg_moved, destination_square_tuple, stacks, on_board_pegs=None, current_location=None):
		"""
		Initializer
		"""
		self.board = board_state
		#Heuristic value: number of options to win (white, black)
		self.hv = hv
		self.peg_moved = peg_moved
		self.destination_square = destination_square_tuple
		self.stacks = stacks
		self.on_board_pegs = on_board_pegs
		self.current_location = current_location


	def __str__(self):
		return "HV: {hv}\nPEG MOVED: {pm}\nDESTINATION: {dest}\n\n".format(hv=self.hv, 
			pm=self.peg_moved, 
			dest=self.destination_square)

		