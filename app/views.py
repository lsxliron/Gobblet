from flask import render_template, url_for, request, jsonify
from app import app
from board import *
from pegstack import *
from gameplay import *
from setgame import *


@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template("index.html")


@app.route('/_place_new_peg_on_board/', methods=['POST'])
def makeMove():
	#Get data from AJAX
	i_position = int(request.form['square_i'])
	j_position = int(request.form['square_j'])
	peg_name = str(request.form['peg'])
		
	#Make a move
	result = mainBoard.place_gobblet_on_sqaure(i_position, j_position, pd[peg_name]);

	#Insert peg to on board dictionary
	if result:
		ob_pd_white[peg_name] = pd[peg_name]
		not_ob_pd_white.pop(peg_name)


	#Check for a winner
	winner = mainBoard.check_winner()
	return jsonify(result=result, winner=winner)
	
	

@app.route('/_reposition_peg_on_board/', methods=['POST'])
def change_peg_position():
	#Get data from AJAX
	old_i_position = int(request.form['square_old_i'])
	old_j_position = int(request.form['square_old_j'])
	new_i_position = int(request.form['square_new_i'])
	new_j_position = int(request.form['square_new_j'])
	

	
	#Make a move
	result = mainBoard.move_peg_on_board(old_i_position,old_j_position, 
										 new_i_position, 
										 new_j_position)
	# print mainBoard
	winner = mainBoard.check_winner()
	return jsonify(result=result, winner=winner)


@app.route('/_reset_board/', methods=['POST'])
def clear_board():
	execfile("setgame.py")
	return "true"

@app.route('/_ai_api/', methods=['POST'])
def ai():
	data = play(mainBoard, pd, ob_pd_black, not_ob_pd_black, 
		        ob_pd_white, not_ob_pd_white,
		        black_pegs_stacks, white_pegs_stacks)


	if data['new_peg']:
		#If move is valid, add peg to on_board dictionary (ob_pd)
		if not_ob_pd_black.has_key(data['peg_name']):
			ob_pd_black[data['peg_name']]=pd[data['peg_name']]
		
			#Remove on board peg from not_on_board dictionay (not_ob_pd)
			not_ob_pd_black.pop(data['peg_name'])

			#Remove peg from peg_stack
			peg_number = int(data['peg_name'][-1:])
			black_pegs_stacks[peg_number-1].pop()
		

	print mainBoard

	return jsonify(result = data['result'],
		           peg_name = data['peg_name'],
		           square = data['square'],
		           winner = data['winner'],
		           new_peg = data['new_peg'])



