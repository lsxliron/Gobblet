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


def play(board, all_pegs, on_board_pegs, off_board_pegs, black_stacks, white_stacks):
	player = "White"
	comp = "Black"
	block_winner = board.three_in_a_row_ai(player)
	peg_name="XXX"
	res = False

	#First move- put one large peg on a random square
	if len(on_board_pegs) == 0:
		i = randint(0,3)
		j = randint(0,3)
		peg_number = randint(1, 3)
		
		peg_object = black_stacks[peg_number-1].top()
		print peg_object
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
		"""nodes_list_new_pegs= list()
		nodes_list_replace_pegs=list()
		if not block_winner:
			#Do possible moves with new pegs
			for i in range(0,15):
				#Get a copy of the current board
				board_copy = copy.deepcopy(board)
				
				#Get the stack number of the biggest peg possible
				biggest_peg = get_biggest_peg_possible(black_stacks)
				
				#Make a move on the board copy
				board_copy.place_gobblet_on_sqaure(i/4,i%4, black_stacks[biggest_peg].top())
				
				#Calculate hv
				hv_tuple = (board_copy.calculate_heuristic("Black"), board_copy.calculate_heuristic("White"))
				#Insert games state to node
				nodes_list_new_pegs.append(Node(board_copy, hv_tuple, black_stacks[biggest_peg].top(), (i/4,i%4)))	

			
			#Do possible moves by replacing gobblets
			board_copy = copy.deepcopy(board)
			#for i in range(0,15):
			for gobblet_to_move in on_board_pegs.values():
				#gobblet_to_move = board_copy.grid[i/4][i%4].stack[board_copy.find_top_peg_on_square(i/4, i%4)]
				
				#if gobblet_to_move != None:
				for k in range(0,4):
					for j in range(0,4):
						#Get a copy of the current board
						board_copy = copy.deepcopy(board)
						#Get the peg to move
						board_copy.move_peg_on_board(i/4,i%4, k,j)
						hv_tuple = (board_copy.calculate_heuristic("Black"), board_copy.calculate_heuristic("White"))
						#Insert state to the nodes list
						nodes_list_replace_pegs.append(Node(board_copy, hv_tuple, gobblet_to_move, (k,j)))"""
		nodes_list_new_pegs=get_hv_list_for_new_pegs(black_stacks, board)
		nodes_list_replace_pegs=get_hv_list_for_replace_pegs(on_board_pegs, board)
		xxx=find_max_hv(nodes_list_new_pegs, "Black")
		yyy=find_max_hv(nodes_list_replace_pegs, "Black")


	pdb.set_trace()



def get_hv_list_for_new_pegs(player_stacks, board):
	nodes_list_new_pegs=list()

	for i in range(0,15):
		#Get a copy of the current board
		board_copy = copy.deepcopy(board)
		
		#Get the stack number of the biggest peg possible
		biggest_peg = get_biggest_peg_possible(player_stacks)
		
		#Make a move on the board copy
		board_copy.place_gobblet_on_sqaure(i/4,i%4, player_stacks[biggest_peg].top())
		
		#Calculate hv
		hv_tuple = (board_copy.calculate_heuristic("Black"), board_copy.calculate_heuristic("White"))
		#Insert games state to node
		nodes_list_new_pegs.append(Node(board_copy, hv_tuple, player_stacks[biggest_peg].top(), (i/4,i%4)))	

	return nodes_list_new_pegs


def get_hv_list_for_replace_pegs(on_board_pegs, board):
	nodes_list_replace_pegs = list()
	board_copy = copy.deepcopy(board)
	for i in range(0,15):
		gobblet_to_move = board_copy.grid[i/4][i%4].stack[board_copy.find_top_peg_on_square(i/4, i%4)]
		if gobblet_to_move != -1:
			for k in range(0,4):
				for j in range(0,4):
					#Get a copy of the current board
					board_copy = copy.deepcopy(board)
					#Get the peg to move
					board_copy.move_peg_on_board(i/4,i%4, k,j)
					hv_tuple = (board_copy.calculate_heuristic("Black"), board_copy.calculate_heuristic("White"))
					#Insert state to the nodes list
					nodes_list_replace_pegs.append(Node(board_copy, hv_tuple, gobblet_to_move, (k,j)))

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
	if player == "White":
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




		
		








