from flask import render_template, url_for, request, jsonify
from app import app
import pdb
from board import *
from gameplay import *


"""
Create pegs and board
"""
mainBoard = Board()


#Tiny white peg
twp1 = Gobblet("White", 1);
twp2 = Gobblet("White", 1);
twp3 = Gobblet("White", 1);

#Small white peg
swp1 = Gobblet("White", 2);
swp2 = Gobblet("White", 2);
swp3 = Gobblet("White", 2);


#Medium white peg
mwp1 = Gobblet("White", 3);
mwp2 = Gobblet("White", 3);
mwp3 = Gobblet("White", 3);

#Big white peg
bwp1 = Gobblet("White", 4);
bwp2 = Gobblet("White", 4);
bwp3 = Gobblet("White", 4);


#Tiny black peg
tbp1 = Gobblet("Black", 1);
tbp2 = Gobblet("Black", 1);
tbp3 = Gobblet("Black", 1);


#Small black peg
sbp1 = Gobblet("Black", 2);
sbp2 = Gobblet("Black", 2);
sbp3 = Gobblet("Black", 2);


#Medium black peg
mbp1 = Gobblet("Black", 3);
mbp2 = Gobblet("Black", 3);
mbp3 = Gobblet("Black", 3);

#Big black peg
bbp1 = Gobblet("Black", 4);
bbp2 = Gobblet("Black", 4);
bbp3 = Gobblet("Black", 4);

'''
PEGS DICTIONARY
'''
pd = dict()

pd['twp1']=twp1
pd['twp2']=twp2
pd['twp3']=twp3


pd['swp1']=swp1
pd['swp2']=swp2
pd['swp3']=swp3

pd['mwp1']=mwp1
pd['mwp2']=mwp2
pd['mwp3']=mwp3


pd['bwp1']=bwp1
pd['bwp2']=bwp2
pd['bwp3']=bwp3

pd['tbp1']=tbp1
pd['tbp2']=tbp2
pd['tbp3']=tbp3

pd['sbp1']=sbp1
pd['sbp2']=sbp2
pd['sbp3']=sbp3


pd['mbp1']=mbp1
pd['mbp2']=mbp2
pd['mbp3']=mbp3


pd['bbp1']=bbp1
pd['bbp2']=bbp2
pd['bbp3']=bbp3

ob_pd = dict()
not_ob_pd = dict()

for key in pd.keys():
	if pd[key].color == 'Black':
		not_ob_pd[key] = pd[key]

print not_ob_pd


@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template("index.html")


@app.route('/_place_new_peg_on_board/', methods=['POST'])
def makeMove():
	#Get data from AJAX
	i_position = int(request.form['square_i'])
	j_position = int(request.form['square_j'])
	peg_name = str(request.form['peg'])
	player = str(request.form['player'])
	pdb.set_trace()
	if player == 'Black':
		print 'PC TURN!!!!!'
		result = play(mainBoard, pd, ob_pd, not_ob_pd)

	'''CREATE A NEW VIEW API WITH AJAX FROM SCRIPTS FOR THE AI'''
	else:
		#Make a move
		result = mainBoard.place_gobblet_on_sqaure(i_position, j_position, pd[peg_name]);

	print mainBoard

	#If move is valid, add peg to on_board dictionary (ob_pd)
	if result and player=='Black':
		print "__________________________________________________"
		print "NOT ON BOARD DICTIONARY"
		print not_ob_pd
		print "__________________________________________________"
		ob_pd[peg_name]=pd[peg_name]

		#Remove on board peg from not_on_board dictionay (not_ob_pd)
		not_ob_pd.pop(peg_name)

	#Check for a winner
	winner = mainBoard.check_winner()
	print ob_pd
	return jsonify(result=result, winner=winner)
	
	

@app.route('/_reposition_peg_on_board/', methods=['POST'])
def change_peg_position():
	#Get data from AJAX
	old_i_position = int(request.form['square_old_i'])
	old_j_position = int(request.form['square_old_j'])
	new_i_position = int(request.form['square_new_i'])
	new_j_position = int(request.form['square_new_j'])
	

	
	#Make a move
	result = mainBoard.move_peg_on_board(old_i_position,old_j_position, new_i_position, new_j_position)
	print mainBoard
	winner = mainBoard.check_winner()
	return jsonify(result=result, winner=winner)


@app.route('/_reset_board/', methods=['POST'])
def clear_board():
	mainBoard.reset()
	print mainBoard
	return "true"
	