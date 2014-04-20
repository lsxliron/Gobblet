from board import *
from gobblet import *
from square import *

b=Board()

g1 = Gobblet("black", 7)
g2 = Gobblet("Blue", 8)
g3 = Gobblet("black", 9)

b.place_gobblet_on_sqaure(0,0,g1)
# b.place_gobblet_on_sqaure(3,0,g2)
b.place_gobblet_on_sqaure(1,0,g1)
b.place_gobblet_on_sqaure(2,0,g1)
b.place_gobblet_on_sqaure(3,0,g1)
print b


print b.winner_row()
print b.winner_col()
