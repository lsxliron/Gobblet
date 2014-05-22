"""
This module create the pegs and board in order to initialize the game.
"""

from board import *
from pegstack import *


global pd
global ob_pd_black
global ob_pd_white
global not_ob_pd_black
global not_ob_pd_white
global black_pegs_stacks
global white_pegs_stacks
global black_stack1
global black_stack2
global black_stack3
global white_stack1
global white_stack2
global white_stack3
global mainBoard

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


ob_pd_black = dict()
ob_pd_white = dict()
not_ob_pd_black = dict()
not_ob_pd_white = dict()


#Create dictionary for pegs on board
for key in pd.keys():
	if pd[key].color == 'Black':
		not_ob_pd_black[key] = pd[key]
	elif pd[key].color == 'White':
		not_ob_pd_white[key] = pd[key]



"""CREATE PEGS STACK"""
black_stack1 = PegStack(pd['bbp1'], pd['mbp1'], pd['sbp1'], pd['tbp1'])
black_stack2 = PegStack(pd['bbp2'], pd['mbp2'], pd['sbp2'], pd['tbp2'])
black_stack3 = PegStack(pd['bbp3'], pd['mbp3'], pd['sbp3'], pd['tbp3'])

white_stack1 = PegStack(pd['bwp1'], pd['mwp1'], pd['swp1'], pd['twp1'])
white_stack2 = PegStack(pd['bwp2'], pd['mwp2'], pd['swp2'], pd['twp2'])
white_stack3 = PegStack(pd['bwp3'], pd['mwp3'], pd['swp3'], pd['twp3'])

black_pegs_stacks = [black_stack1, black_stack2, black_stack3]
white_pegs_stacks = [white_stack1, white_stack2, white_stack3]