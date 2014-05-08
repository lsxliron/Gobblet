"""
This class is the AI of the game.
All the functions is this class are to calculate heuristics values
and choose the right moves
"""
from board import *
from square import *
from gobblet import *
from node import *
import copy
from random import randint
import time


def play(board, all_pegs, on_board_pegs_black, off_board_pegs_black, 
	     on_board_pegs_white, off_board_pegs_white, 
	     black_stacks, white_stacks):
	player = "White"
	comp = "Black"
	block_winner = board.three_in_a_row_ai(player)
	res = False
	winning_move = board.three_in_a_row_ai()
	print "___________________________________________________"
	print "___________________________________________________"
	print winning_move
	print "___________________________________________________"
	print "___________________________________________________"
	

	#First move- put one large peg on a random square
	if len(on_board_pegs_black) == 0:
		i = randint(0,3)
		j = randint(0,3)
		peg_number = randint(1, 3)
		
		peg_object = black_stacks[peg_number-1].top()

		for key,value in all_pegs.iteritems():
			if value == peg_object:
				peg_name = key

		#Make a random move as a begining. The while loop is in case
		#the move is not valid
		while not res:
			res = board.place_gobblet_on_sqaure(i, j, all_pegs[peg_name])

		winner = board.check_winner()

		data = dict()
		data['result'] = res;
		data['peg_name'] = peg_name;
		data['square'] = str(i)+str(j)
		data['winner'] = winner
		data['new_peg'] = True
		#time.sleep(2)
		return data

	
	else:
		nodes_list_new_pegs= list()
		nodes_list_replace_pegs=list()
	
		nodes_list_new_pegs_black = get_hv_list_for_new_pegs(black_stacks, board)
		nodes_list_replace_pegs_black = get_hv_list_for_replace_pegs(on_board_pegs_black, board, all_pegs)
		max_replace = find_max_hv(nodes_list_replace_pegs_black,"Black")
		max_new = find_max_hv(nodes_list_new_pegs_black,"Black")
		if max_replace != 100:
			max_replace_value = nodes_list_replace_pegs_black[max_replace].hv[1]
		else: 
			max_replace_value = -1
		max_new_value = nodes_list_new_pegs_black[max_new].hv[1]


		#-------------------#
		#Find the best move #
		#-------------------#

		
		#Make a winning move if possible:

		if winning_move:
			if winning_move.has_key("row"):
				winning_square = winning_move["row"]
			elif winning_move.has_key("col"):
				winning_square = winning_move["col"]
			#Find the biggest peg possible to add to the board
			gb = black_stacks[get_biggest_peg_possible(black_stacks)].top()
			
			print gb
			
			for key, value in off_board_pegs_black.iteritems():
				if gb is value:
					peg_name = key

			res = board.place_gobblet_on_sqaure(winning_square[0], winning_square[1], gb)

			if res:
				data = dict()
				data['result'] = res
				data['peg_name'] = peg_name;
				data['square'] = str(winning_square[0])+str(winning_square[1])
				data['winner'] = board.check_winner()
				data['new_peg'] = False
				return data



		# if max_replace_value>max_new_value:
		if max_replace_value < max_new_value and not res:  
			node = nodes_list_new_pegs_black[max_new]
			
			#Get peg name
			for key, value in off_board_pegs_black.iteritems():
				if value == node.peg_moved:
					peg_name=key
			
			gb = node.peg_moved

			square = node.destination_square

			# pdb.set_trace()

			res = board.place_gobblet_on_sqaure(square[0],square[1],gb)
			winner = board.check_winner()
			
			print "BLACK IN MOVING {pn} TO ({i}, {j})".format(pn=peg_name, i=square[0], j=square[1])
			data = dict()
			data['result'] = res;
			data['peg_name'] = peg_name;
			data['square'] = str(square[0])+str(square[1])
			data['winner'] = winner
			data['new_peg'] = True
			#time.sleep(2)
			return data


		#Replace peg on board
		elif max_replace_value >= max_new_value:
			
			# pdb.set_trace()
			node = nodes_list_replace_pegs_black[max_replace]
			
			
			gb = board.find_top_peg_on_square(node.current_location[0],node.current_location[1])
			# pdb.set_trace()
			#Get peg name
			for key, value in on_board_pegs_black.iteritems():# off_board_pegs_black.iteritems():
				if value is board.grid[node.current_location[0]][node.current_location[1]].stack[gb]:
					peg_name=key


			square = node.destination_square
			current_location = node.current_location

			

			res = board.move_peg_on_board(current_location[0],current_location[1],square[0],square[1])
			winner = board.check_winner()
			print "________________________________________________________________________"
			print res
			print "________________________________________________________________________"
			
			print "BLACK IN RE-MOVING {pn} FROM ({i1},{j1}) TO ({i2}, {j2})".format(pn=peg_name,i1=current_location[0],j1=current_location[1], i2=square[0], j2=square[1])
			data = dict()
			if res == 1:
				res_return = True
			else:
				res_return = False

			data['result'] = res_return;
			data['peg_name'] = peg_name;
			data['square'] = str(square[0])+str(square[1])
			data['winner'] = winner
			data['new_peg'] = False
			#time.sleep(2)
			
			return data


		else:
			print "PROBLEM!!!"
			pdb.set_trace()
















def get_hv_list_for_new_pegs(player_stacks, board):

	nodes_list_new_pegs=list()

	for j in range(0,3):
		biggest_peg = get_biggest_peg_possible(player_stacks)
		for i in range(0,15):
			
			#Get a copy of the current board
			board_copy = copy.deepcopy(board)
						
			#Make a move on the board copy
			move = board_copy.place_gobblet_on_sqaure(i/4,i%4, player_stacks[biggest_peg].top())
			
			#Calculate hv
			hv_tuple = (board_copy.calculate_heuristic("White"), board_copy.calculate_heuristic("Black"))
			
			#Create a node for game state
			if move:
				nodes_list_new_pegs.append(Node(board_copy, hv_tuple, player_stacks[biggest_peg].top(), (i/4,i%4), player_stacks))	

	return nodes_list_new_pegs



def get_hv_list_for_replace_pegs(on_board_pegs, board, all_pegs):
	nodes_list_replace_pegs = list()
	
	# pdb.set_trace()
	for peg in on_board_pegs.values():
		#get the current peg location
		# pdb.set_trace()
		board_copy = copy.deepcopy(board)
		
		for i in range(0,4):
			for j in range(0,4):
				peg_to_move_temp = board.grid[i][j].stack[board.find_top_peg_on_square(i,j)]
				if peg is peg_to_move_temp:
					current_location = (i, j)
					peg_to_move = peg_to_move_temp
		
		for i in range(0,4):
			for j in range(0,4):
				board_copy = copy.deepcopy(board)
				hv_tuple = (board_copy.calculate_heuristic("White"), 
					        board_copy.calculate_heuristic("Black"))

				move = board_copy.move_peg_on_board(current_location[0], current_location[1],i,j)
				
				if move == 1:
					nodes_list_replace_pegs.append(Node(board_copy, hv_tuple, peg_to_move, (i,j), None, on_board_pegs, (current_location[0],current_location[1])))

	return nodes_list_replace_pegs



def get_biggest_peg_possible(stacks_list):
	"""
	Returns the stack number of the biggest peg possible
	"""
	biggest = 0

	for i in range(0,2):
		temp = stacks_list[i].top()
		if temp>biggest:
			biggest = temp
			stack_number = i
	return stack_number

def find_max_hv(nodes_list, player):
	"""
	Return the index of the highes hv in the nodes list
	"""

	if len(nodes_list) == 0:
		return 100
	elif player == "White":
		index = 0
	else:
		index = 1

	max_hv = nodes_list[0].hv[index]
	max_hv_index = 0

	for i in range(0, len(nodes_list)):
		if max_hv < nodes_list[i].hv[index]:
			max_hv = nodes_list[i].hv[index]
			max_hv_index = i

	return max_hv_index

def find_min_hv(nodes_list, player):
	"""
	Return the index of the highes hv in the nodes list
	"""
	if player == "White":
		index = 0
	else:
		index = 1

	min_hv = nodes_list[0].hv[index]
	min_hv_index = 0

	for i in range(0, len(nodes_list)):
		if min_hv > nodes_list[i].hv[index]:
			min_hv = nodes_list[i].hv[index]
			min_hv_index = i

	return min_hv_index