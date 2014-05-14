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
	res = False	
	winning_move_blocker = board.three_in_a_row_ai()
	winning_move = board.three_in_a_row_ai()
	# PC_winning_move = board.three_in_a_row_ai("White")
	winning_square = None
	
	

	#First move- put one large peg on a random square
	pdb.set_trace()
	if len(on_board_pegs_black) == 0:
		# i = randint(0,3)
		# j = randint(0,3)
		# i=2
		# j=1
		peg_number = randint(1, 3)
		res = False

		peg_object = black_stacks[peg_number-1].top()

		#Get peg name
		for key,value in all_pegs.iteritems():
			if value == peg_object:
				peg_name = key
		#Make a random move as a begining. The while loop is in case
		#the move is not valid
		while not res:
			i = randint(0,3)
			j = randint(0,3)
			# i=2
			# j=1
			
			#Perform move
			res = board.place_gobblet_on_sqaure(i, j, all_pegs[peg_name])

		
		#Check for winner
		winner = board.check_winner()

		#Return JSON
		data = dict()
		data['result'] = res;
		data['peg_name'] = peg_name;
		data['square'] = str(i)+str(j)
		data['winner'] = winner
		data['new_peg'] = True
		return data

	# if PC_winning_move:
	# 	if PC_winning_move.has_key('row'):
	# 		PC_winning_square = PC_winning_move['row']
	# 	elif PC_winning_move.has_key('col'):
	# 		PC_winning_square = PC_winning_move['col']
	# 	elif PC_winning_move.has_key('diag'):
	# 		PC_winning_square = PC_winning_move['diag']



	# 	peg = black_stacks[get_biggest_peg_possible(black_stacks)].top()
		
	# 	for key, value in off_board_pegs_black.iteritems():
	# 				if peg is value:
	# 					peg_name = key
	# 	res = board.place_gobblet_on_sqaure(PC_winning_square[0],PC_winning_square[1],peg)
	# 	if res:
	# 		data = dict()
	# 		data['result'] = res
	# 		data['peg_name'] = peg_name;
	# 		data['square'] = str(PC_winning_square[0])+str(PC_winning_square[1])
	# 		data['winner'] = board.check_winner()
	# 		data['new_peg'] = True

	# 		# pdb.set_trace()
	# 		return data



	if winning_move:
		if winning_move.has_key('row'):
			if board.grid[winning_move['row'][0]][winning_move['row'][1]].stack[board.find_top_peg_on_square(winning_move['row'][0],winning_move['row'][1])].color != "Black":
				winning_square = winning_move['row']
				forbidden = winning_square[0]
		
		if winning_move.has_key('col'):
			if board.grid[winning_move['col'][0]][winning_move['col'][1]].stack[board.find_top_peg_on_square(winning_move['col'][0],winning_move['col'][1])].color != "Black":
				winning_square = winning_move['col']
				forbidden = winning_square[1]
		
		if winning_move.has_key('diag'):
			if board.grid[winning_move['diag'][0]][winning_move['diag'][1]].stack[board.find_top_peg_on_square(winning_move['diag'][0],winning_move['diag'][1])].color != "Black":
				winning_square = winning_move['diag']


	if winning_square:
		# temp_size = 0
		# temp_color=None
		temp = board.grid[winning_square[0]][winning_square[1]].stack[board.find_top_peg_on_square(winning_square[0],winning_square[1])]
		# if temp != "(free)":
		# 	temp_size = temp.size
		# 	temp_color = temp.color
		# if board.find_top_peg_on_square(winning_square[0],winning_square[1]).size != 4:
		if temp.size != 4 or temp.color != 'Black':
			
			#Case that there are no pegs to reposition on the board- place a new peg
			if len(on_board_pegs_black)<4 or board.grid[winning_square[0]][winning_square[1]].empty():
				peg_index = get_biggest_peg_possible(black_stacks)
				peg = black_stacks[peg_index].top()
				
				#Get peg name
				for key, value in off_board_pegs_black.iteritems():
					if peg == value:
						peg_name = key

				res = board.place_gobblet_on_sqaure(winning_square[0], winning_square[1], peg)
				winner = board.check_winner()
				if res:
					data = dict()
					data['result'] = res
					data['peg_name'] = peg_name;
					data['square'] = str(winning_square[0])+str(winning_square[1])
					data['winner'] = winner
					data['new_peg'] = True

					# pdb.set_trace()
					return data

		# #Position is already blocked, place new peg on the board
		# else:
		# 	res=False
		# 	nodes_list_new_pegs_black = get_hv_list_for_new_pegs(black_stacks, board)
		# 	max_new = find_max_hv(nodes_list_new_pegs_black,"Black")
		# 	node = nodes_list_new_pegs_black[max_new]
		# 	square = node.destination_square
		# 	while square[0] == winning_square[0] and square[1] == winning_square[1]
		# 	peg = node.peg_moved
		# 	res = board.place_gobblet_on_sqaure(square[0], square[1], peg)
		# 	for key, value in off_board_pegs_black.iteritems():
		# 		if peg is value:
		# 			peg_name = key


		# 	if  res:
		# 		data = dict()
		# 		data['result'] = res
		# 		data['peg_name'] = peg_name;
		# 		data['square'] = str(winning_square[0])+str(winning_square[1])
		# 		data['winner'] = board.check_winner()
		# 		data['new_peg'] = True
		# 		return data






	if not res:
	# else:
		#Setup variables
		# nodes_list_new_pegs= list()
		# nodes_list_replace_pegs=list()
	
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
		pdb.set_trace()
		print winning_move
		if winning_move:
			pdb.set_trace()
			if winning_move.has_key("row"):
				winning_square = winning_move["row"]
			elif winning_move.has_key("col"):
				winning_square = winning_move["col"]
			elif winning_move.has_key("diag"):
				winning_square = winning_move["diag"]

			print "WINNING MOVE:"
			print winning_move

		if winning_move and board.grid[winning_square[0]][winning_square[1]].stack[board.find_top_peg_on_square(winning_square[0],winning_square[1])].color!="Black":

			#Find the biggest peg possible to add to the board
			gb = black_stacks[get_biggest_peg_possible(black_stacks)].top()
			
			#Get peg name
			for key, value in off_board_pegs_black.iteritems():
				if gb is value:
					peg_name = key
			
			##########
			#ROW CASE#
			##########
			keep_looking = True
			valid_res = False
			forbidden_row = winning_square[0]
			opponent_peg_size = board.grid[winning_square[0]][winning_square[1]].stack[board.find_top_peg_on_square(winning_square[0],winning_square[1])].size
			
			if winning_move.has_key("diag"):
				res = board.place_gobblet_on_sqaure(winning_square[0], winning_square[1], gb)
				if res:
					valid_res=True
					winner = board.check_winner()
			
			if opponent_peg_size == 4 and not valid_res: #Can't cover the largest peg
				winner = False
				res = False
				for i in range(0,4):
					for j in range(0,4):
						loose = True
						board_copy = copy.deepcopy(board)
						# pdb.set_trace()
						if i != forbidden_row and (res != 1 or res != 2) and keep_looking and (i!=winning_square[0] and j!= winning_square[1]):
							top_peg = board.grid[i][j].stack[board.find_top_peg_on_square(i,j)]
							loose =board.three_in_a_row(i,j,top_peg,"White")
							# pdb.set_trace()
							
							if top_peg.color == "Black" and top_peg.size>opponent_peg_size and not loose and (i!= winning_square[0] and j!= winning_square[1]):
								# pdb.set_trace()
								res = board_copy.move_peg_on_board(i,j,winning_square[0], winning_square[1])
								#Get peg name
								if res !=0:
									for key, value in on_board_pegs_black.iteritems():
										if value is top_peg:
											peg_name = key
											valid_res = res
											keep_looking = False
											winner = board_copy.check_winner()
									
				
			#Return JSON to jQuery
			if valid_res:
				data = dict()
				data['result'] = valid_res
				data['peg_name'] = peg_name;
				data['square'] = str(winning_square[0])+str(winning_square[1])
				data['winner'] = winner
				data['new_peg'] = True

				# pdb.set_trace()
				return data



		#Block the player from making a winning move
		
		if winning_move_blocker!= False :
			if winning_move_blocker.has_key("row"):
				winning_square = winning_move_blocker["row"]
			elif winning_move_blocker.has_key("col"):
				winning_square = winning_move_blocker["col"]

			elif winning_move_blocker.has_key("diag"):
				winning_square = winning_move_blocker["diag"]
			

			if winning_square and not (board.grid[winning_square[0]][winning_square[1]].stack[board.find_top_peg_on_square(winning_square[0],winning_square[1])].color=='Black'):
			


				print "===winning_move_blocker==="
				# x = winning_move_blocker['row'][0]
				# y = winning_move_blocker['row'][1]
				#Check that winning move was not blocked already
				
				
				# if winning_move_blocker.has_key("row"):
				# 	winning_square = winning_move_blocker["row"]
				# elif winning_move_blocker.has_key("col"):
				# 	winning_square = winning_move_blocker["col"]

				# elif winning_move_blocker.has_key("diag"):
				# 	winning_square = winning_move_blocker["diag"]

				#Find the biggest peg possible to add to the board
				gb = black_stacks[get_biggest_peg_possible(black_stacks)].top()
				
				#Get peg name
				for key, value in off_board_pegs_black.iteritems():
					if gb is value:
						peg_name = key

				#Perform the move
				res = board.place_gobblet_on_sqaure(winning_square[0], winning_square[1], gb)
				winner = board.check_winner()
				#Return JSON to jQuery
				if res:
					data = dict()
					data['result'] = res
					data['peg_name'] = peg_name;
					data['square'] = str(winning_square[0])+str(winning_square[1])
					data['winner'] = board.check_winner()
					data['new_peg'] = True
					return data



		
		if max_replace_value < max_new_value and not res:  
			node = nodes_list_new_pegs_black[max_new]
			print node.current_location

			# if winning_move_blocker:
			# 	x = winning_move_blocker['row'][0]
			# 	y = winning_move_blocker['row'][1]
				
				
				
			# 	if winning_move_blocker:
			# 		if winning_move_blocker.has_key('row'):
			# 			# while winning_move_blocker['row'][0] == node.current_location[0] and winning_move_blocker['row'][1] == node.current_location[1]:
			# 			while node.peg_moved is board.grid[x][y].stack[board.find_top_peg_on_square(x,y)]:
			# 				nodes_list_replace_pegs_black.remove(nodes_list_replace_pegs_black[max_replace])
			# 				max_replace = find_max_hv(nodes_list_replace_pegs_black,"Black")
			# 				node = nodes_list_replace_pegs_black[max_replace]



			#Get peg name	
			for key, value in off_board_pegs_black.iteritems():
				if value is node.peg_moved:
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


		#Reposition peg on board
		elif max_replace_value >= max_new_value:
			
			
			node = nodes_list_replace_pegs_black[max_replace]
			square = node.destination_square
			
			current_location = node.current_location
			res = False
			loose = True
			peg_name=None
			#do_once=False

			node = nodes_list_replace_pegs_black[max_replace]
			gb = board.find_top_peg_on_square(node.current_location[0],node.current_location[1])

			#Case that the destination and the current location are the same
			while (current_location[0] == square[0] and current_location[1] == current_location[1]) or loose and current_location == winning_square:
				#do_once=False
				nodes_list_replace_pegs_black.remove(nodes_list_replace_pegs_black[max_replace])
				max_replace = find_max_hv(nodes_list_replace_pegs_black, "Black")
				max_replace_value = nodes_list_replace_pegs_black[max_replace].hv[1]
				node = nodes_list_replace_pegs_black[max_replace]
				square = node.destination_square
				current_location = node.current_location
				# loose = board.three_in_a_row(square[0], square[1], gb, 'White')
				# loose = board.three_in_a_row(current_location[0], current_location[1], gb, 'Black')
				loose = current_location==winning_square

				gb = board.find_top_peg_on_square(node.current_location[0],node.current_location[1])
			
				#Get peg name
				for key, value in on_board_pegs_black.iteritems():# off_board_pegs_black.iteritems():
					if value is board.grid[node.current_location[0]][node.current_location[1]].stack[gb]:
						peg_name=key
				board_copy = copy.deepcopy(board)
				res = board_copy.move_peg_on_board(current_location[0],current_location[1],square[0],square[1])
			

			if not peg_name:
				#Get peg name
				for key, value in on_board_pegs_black.iteritems():# off_board_pegs_black.iteritems():
					if value is board.grid[node.current_location[0]][node.current_location[1]].stack[gb]:
						peg_name=key

			#Case the while loop didn't execute
			
			res = board.move_peg_on_board(current_location[0],current_location[1],square[0],square[1])


			winner = board.check_winner()
			
			print "BLACK IN RE-MOVING {pn} FROM ({i1},{j1}) TO ({i2}, {j2})".format(pn=peg_name,i1=current_location[0],j1=current_location[1], i2=square[0], j2=square[1])
			data = dict()
			if res != 0:
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
				nodes_list_new_pegs.append(Node(board_copy, hv_tuple, player_stacks[biggest_peg].top(), (i/4,i%4), player_stacks, None, (i/4,i%4)))	

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

# def checK_if_loose_move(board, peg, i, j, player="White"):
# 	"""
# 	Returns true if removing peg will result in three in a row for the opponent
# 	"""

# 	row_list = list()
# 	col_list = list()
# 	for i in range(0,4):
# 		row_list.append(board.grid[i][j].stack[board.find_top_peg_on_square(i,j)]).color

	










