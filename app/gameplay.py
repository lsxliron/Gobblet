from board import *
from square import *
from gobblet import *
from node import *
import copy
from random import randint
import time





def play(board, all_pegs, on_board_pegs, off_board_pegs, black_stacks, white_stacks):
	player = "White"
	comp = "Black"
	block_winner = board.three_in_a_row_ai(player)
	#First move- put one large peg on a random square
	
	if len(on_board_pegs) == 0:
		i = randint(0,3)
		j = randint(0,3)
		peg_number = randint(1, 3)
		peg_name = "bbp" + str(peg_number)
		res = board.place_gobblet_on_sqaure(i, j, all_pegs[peg_name])
		winner = board.check_winner()

		data = dict()
		data['result'] = res;
		data['peg_name'] = peg_name;
		data['square'] = str(i)+str(j)
		data['winner'] = winner
		data['new_peg'] = True
		time.sleep(2)
		return data

		
	else:
		nodes_list_new_pegs= list()
		nodes_list_replace_pegs=list()
		if not block_winner:
			for i in range(0,15):
				#Get a copy of the current board
				board_copy = copy.deepcopy(board)
				
				nodes_list.append(board_copy.calculate_hueristic("Black"), board_copy.calculate_hueristic("White"))





		# elif block_winner:
		#look for the smallest peg you can put to block winning
		# smallest = 4
		# for i in range(0,4):
		# 	for peg in on_board_pegs.keys():
		# 		temp = int(peg[len(peg)-1:len(peg)])
		# 		smallest = min(smallest,temp)




		



	# else:
		#Get a copy of the current board
		board_copy = copy.deepcopy(board)

