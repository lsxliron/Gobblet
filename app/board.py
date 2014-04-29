from square import *
from gobblet import *
from collections import Counter



class Board(object):
	
	def __init__(self):
		"""
		Initializer
		"""
		self.grid=list()
		for i in range(0,4):
			self.grid.append(list())
			for j in range(0,4):
				self.grid[i].append(Square())


	def __str__(self):
		"""
		print function
		"""
		output = ""
		for i in range(0,4):
			for j in range(0,4):
				output += str(self.grid[i][j]) + " "
			output += "\n"
		return output

	def three_in_a_row(self,i,j, gb):
		"""
		returns true if the opponent can make a winner move
		"""

		#Get the opponent color
		if gb.color == "White":
			color = "Black"
		else:
			color = "White"

		row_gobblet_list = list()
		col_gobblet_list = list()

		#get column gobblets
		col_gobblet_list.append(self.grid[i][0].stack[self.find_top_peg_on_square(i,0)].color)
		col_gobblet_list.append(self.grid[i][1].stack[self.find_top_peg_on_square(i,1)].color)
		col_gobblet_list.append(self.grid[i][2].stack[self.find_top_peg_on_square(i,2)].color)
		col_gobblet_list.append(self.grid[i][3].stack[self.find_top_peg_on_square(i,3)].color)

		#get row gobblets
		row_gobblet_list.append(self.grid[0][j].stack[self.find_top_peg_on_square(0,j)].color)
		row_gobblet_list.append(self.grid[1][j].stack[self.find_top_peg_on_square(1,j)].color)
		row_gobblet_list.append(self.grid[2][j].stack[self.find_top_peg_on_square(2,j)].color)
		row_gobblet_list.append(self.grid[3][j].stack[self.find_top_peg_on_square(3,j)].color)


		if col_gobblet_list.count(color) == 3 or row_gobblet_list.count(color) == 3:
			return True

		return False

	def place_gobblet_on_sqaure(self, i, j, gb):
		"""
		Place a peg on the board if the move is legal
		"""
		
		#Legal move- placing a new peg on an occupied square
		#when opponent has 3 pegs in a row
		if self.three_in_a_row(i,j,gb):
			return True

		#Illega move- trying to place a new gobblet on an 
		#occupied square
		if not self.grid[i][j].empty():
			return False


		#Make sure the square is not full
		if self.grid[i][j].full():
			return False

		# Make sure the pegs are different colors (no white on white/ black on black)
		# top_gobblet_index = self.find_top_peg_on_square(i, j)
		# if self.grid[i][j].stack[top_gobblet_index].color == gb.color:
			# return False


		#First peg in the square- occupy if it's free'
		elif self.grid[i][j].empty():
			self.grid[i][j].stack[0] = gb
			return True

		else:
			#Find the next level to place the peg
			for k in range(1,4):

				if self.grid[i][j].stack[k].dummy():
					#Check that the spot is valid
					#i.e not small peg on top of big peg
					if gb.size > self.grid[i][j].stack[k-1].size:
						self.grid[i][j].stack[k] = gb
						return True

					#Case that trying to put a small peg on top of a bigger one
					else:
						return False
		return False


	



		


	# def move_peg_on_board(self, old_i, old_j, new_i, new_j):
	# 	"""
	# 	Moves peg from (old_i, old_j) to (new_i, new_j) if the move is legal
	# 	"""
	# 	peg_to_move_index = self.find_top_peg_on_square(old_i,old_j)
	# 	#Copy of the gobblet to move
	# 	if peg_to_move_index != -1:
	# 		new_gobblet = Gobblet(-1,-1,self.grid[old_i][old_j].stack[peg_to_move_index])
		
	# 		if self.place_gobblet_on_sqaure(new_i, new_j, new_gobblet):
	# 			#Remove the gobblet from the old location
	# 			self.grid[old_i][old_j].stack[peg_to_move_index]=Gobblet()
	# 			return True
	# 	return False

	def move_peg_on_board(self, old_i, old_j, new_i, new_j):
		"""
		Moves peg from (old_i, old_j) to (new_i, new_j) if the move is legal
		Returns: 
			0 for illegal
			1 for legal move
			2 when player reveal opponent peg and opponent wins

		"""
		peg_to_move_index = self.find_top_peg_on_square(old_i,old_j)
		#Copy of the gobblet to move
		if peg_to_move_index != -1:
			new_gobblet = Gobblet(-1,-1,self.grid[old_i][old_j].stack[peg_to_move_index])
		
			if self.place_gobblet_on_sqaure(new_i, new_j, new_gobblet):
				#Remove the gobblet from the old location
				self.grid[old_i][old_j].stack[peg_to_move_index]=Gobblet()

				#if player reveal opponent peg and opponent wins
				if self.check_winner():
					return 2
				return 1
		
		return 0

	




	def find_top_peg_on_square(self, i, j):
		"""
		Finds the top peg on a given square
		Returns the stack level of the last peg of -1 if the square is empty
		"""
		top = -1 	#Holds the top peg

		if self.grid[i][j].empty():
			return -1

		for k in range(0,4):
			if not self.grid[i][j].stack[k].dummy():
				top = k

		return top


	def winner_row(self):
		"""
		Returns true if there is a winning row or false otherwise
		We create a list of booleans for the board rows. If there exists
		a True row then there is a winner.
		"""
		full_row = list()

		#Check if there exists a winning row
		for i in range(0,4):
			winner = True
			for j in range(0,3):
				#Case that the square is not empty
				if not self.grid[i][j].empty():
					#get the top gobblet on the square
					current_top_gobblet_index = self.find_top_peg_on_square(i,j)
					next_top_gobblet_index = self.find_top_peg_on_square(i,j+1)

					#Check if gobblets have the same colors
					if self.grid[i][j].stack[current_top_gobblet_index].color != self.grid[i][j+1].stack[next_top_gobblet_index].color:
						winner = False
				#Case the square is empty- impossible to be a winning row
				else:
					winner = False

			full_row.append(winner)

		return True in full_row


	def winner_col(self):
		"""
		Returns true if there is a winning column or false otherwise
		We create a list of booleans for the board columns. If there exists
		a True row then there is a winner.
		"""
		
		#If we have empty square on a col this col can't be a winner
		exists_empty_squares = False
		
		for i in range(0,4):
			full_col = list()	#Holds the top pegs colors for the current row
			for j in range(0,4):
				if self.grid[j][i].empty():
					exists_empty_squares = True

			if not exists_empty_squares:
				first_top_gobblet_index = self.find_top_peg_on_square(0,i)
				second_top_gobblet_index = self.find_top_peg_on_square(1,i)
				third_top_gobblet_index = self.find_top_peg_on_square(2,i)
				fourth_top_gobblet_index = self.find_top_peg_on_square(3,i)

				full_col.append(self.grid[0][i].stack[first_top_gobblet_index].color)
				full_col.append(self.grid[1][i].stack[second_top_gobblet_index].color)
				full_col.append(self.grid[2][i].stack[third_top_gobblet_index].color)
				full_col.append(self.grid[3][i].stack[fourth_top_gobblet_index].color)

				#Check that all the colors a the same
				if full_col.count(full_col[0]) == len(full_col):
					return True

			exists_empty_squares=False

		return False

	def winner_diag(self):
		"""
		Returns true if a player wins diagonally and false otherwise
		"""
		colors_list = list()
		
		#First diagonal
		for i in range(0,4):
			colors_list.append(self.grid[i][i].stack[self.find_top_peg_on_square(i,i)].color)
		
		if colors_list[0] != -1 and colors_list.count(colors_list[0]) == 4:
			return True

		#second diagonal
		colors_list=list()
		k = 3
		for i in range(0,4):
			colors_list.append(self.grid[k][i].stack[self.find_top_peg_on_square(k,i)].color)
			k -= 1

		if colors_list[0] != -1 and colors_list.count(colors_list[0]) == 4:
			return True

		return False


	def check_winner(self):
		"""
		Returns true if there exist a winner or false otherwise
		"""
		column_winner = self.winner_col()
		row_winner = self.winner_row()
		diag_winner = self.winner_diag()
		return column_winner or row_winner or diag_winner

	def reset(self):
		"""
		Returns an empty board
		"""
		self.__init__();


	def calculate_heuristic(self):
		"""
		Calculate the heuristic value (hv)
		The hv is the number of possible winning rows or columns for the player
		"""
		hv = 0;
		col = list()
		row=list()

		#Checking possible winning cols
		for i in range(0,4):
			#Get colors
			count_dict=None
			first_top_gobblet_index = self.find_top_peg_on_square(0,i)
			second_top_gobblet_index = self.find_top_peg_on_square(1,i)
			third_top_gobblet_index = self.find_top_peg_on_square(2,i)
			fourth_top_gobblet_index = self.find_top_peg_on_square(3,i)


			col.append(self.grid[0][i].stack[first_top_gobblet_index].color)
			col.append(self.grid[1][i].stack[second_top_gobblet_index].color)
			col.append(self.grid[2][i].stack[third_top_gobblet_index].color)
			col.append(self.grid[3][i].stack[fourth_top_gobblet_index].color)


			count_dict = Counter(col) #perform the count

			#if the column is possible to be winning increase hv
			if not count_dict.has_key('Black') and count_dict.has_key('White'):
				hv += 1
			
			col = list()	#reset list

		#Checking possible winning cols
		for i in range(0,4):
			count_dict=dict()
			first_top_gobblet_index = self.find_top_peg_on_square(i, 0)
			second_top_gobblet_index = self.find_top_peg_on_square(i, 1)
			third_top_gobblet_index = self.find_top_peg_on_square(i, 2)
			fourth_top_gobblet_index = self.find_top_peg_on_square(i, 3)


			row.append(self.grid[i][0].stack[first_top_gobblet_index].color)
			row.append(self.grid[i][1].stack[second_top_gobblet_index].color)
			row.append(self.grid[i][2].stack[third_top_gobblet_index].color)
			row.append(self.grid[i][3].stack[fourth_top_gobblet_index].color)


			count_dict = Counter(row)	#perform the count

			#if the row is possible to be winning increase hv
			if not count_dict.has_key('Black') and count_dict.has_key('White'):
				hv += 1

			row = list()	#reset list
			


		return hv

