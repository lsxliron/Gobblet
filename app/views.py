from flask import render_template, url_for, request, jsonify
from app import app
import pdb
from board import *


"""
Create pegs and board
"""
mainBoard = Board()


#Small white peg
swp1 = Gobblet("White", 1);
swp2 = Gobblet("White", 1);
swp3 = Gobblet("White", 1);
swp4 = Gobblet("White", 1);

#Medium white peg
mwp1 = Gobblet("White", 2);
mwp2 = Gobblet("White", 2);
mwp3 = Gobblet("White", 2);
mwp4 = Gobblet("White", 2);

#Big white peg
bwp1 = Gobblet("White", 3);
bwp2 = Gobblet("White", 3);
bwp3 = Gobblet("White", 3);
bwp4 = Gobblet("White", 3);

#Small black peg
sbp1 = Gobblet("Black", 1);
sbp2 = Gobblet("Black", 1);
sbp3 = Gobblet("Black", 1);
sbp4 = Gobblet("Black", 1);

#Medium black peg
mbp1 = Gobblet("Black", 2);
mbp2 = Gobblet("Black", 2);
mbp3 = Gobblet("Black", 2);
mbp4 = Gobblet("Black", 2);

#Big black peg
bbp1 = Gobblet("Black", 3);
bbp2 = Gobblet("Black", 3);
bbp3 = Gobblet("Black", 3);
bbp4 = Gobblet("Black", 3);

'''
PEGS DICTIONARY
'''
pd = dict()

pd['swp1']=swp1
pd['swp2']=swp2
pd['swp3']=swp3
pd['swp4']=swp4

pd['mwp1']=mwp1
pd['mwp2']=mwp2
pd['mwp3']=mwp3
pd['mwp4']=mwp4

pd['bwp1']=bwp1
pd['bwp2']=bwp2
pd['bwp3']=bwp3
pd['bwp4']=bwp4

pd['sbp1']=sbp1
pd['sbp2']=sbp2
pd['sbp3']=sbp3
pd['sbp4']=sbp4

pd['mbp1']=mbp1
pd['mbp2']=mbp2
pd['mbp3']=mbp3
pd['mbp4']=mbp4

pd['bbp1']=bbp1
pd['bbp2']=bbp2
pd['bbp3']=bbp3
pd['bbp4']=bbp4

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

	print mainBoard
	'''
	add check winner and return with json to jquery
	'''
	return jsonify(result=result)
	
	

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
	'''
	add check winner and return with json to jquery
	'''
	return jsonify(result=result)


	
	