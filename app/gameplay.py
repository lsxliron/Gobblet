from board import *
from square import *
from gobblet import *
import copy
from random import randint


def play(board, all_pegs, on_board_pegs, off_board_pegs):
	if len(on_board_pegs) == 0:
		#CHECK PEGS COLORS ON THE IF STATEMENT
		i = randint(0,3)
		j = randint(0,3)
		res = board.place_gobblet_on_sqaure(i, j, all_pegs['bbp3']);
		print res
		return res



	else:
		#Get a copy of the current board
		board_copy = copy.deepcopy(board)

