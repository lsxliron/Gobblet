from flask import render_template, url_for, request
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

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template("index.html")


# @app.route('/', methods='POST')
# def makeMove():
	