
class node(object):
	def __init__(self, white_hv, black_hv):
		board_state = None
		#Heuristic value: number of options to win (white, black)
		hv = [0, 0]
