# Gobblet Game- Human Vs. PC #

## About This Project##
This web application was created as a project in AI course with another classmate.  

This project is written in *python* and using the [Flask](http://flask.pocoo.org) framework.

If you are not familiar with this game you can read about at [Blue Orange Games](http://en.whttp://www.blueorangegames.com/index.php/games/gobblet) website.

#### Project Outline####
This project is an actual goblet game between the user and the PC.  
The method used for this project is [*MiniMax*](http://en.wikipedia.org/wiki/Bahttp://en.wikipedia.org/wiki/Minimax)

##Installation##
After cloneining the repository, navigate to the repository folder and type:
```
virtualenv --no-site-packages .gobblet && source .gobblet/bin/activate && pip install -r requirements.txt
```
##Usage##
Start the app by typing 
```
python runserver.py
```

##Rules##
###Goal:###
This game is a complex version of Tic Tac Toe game. The game uses a 4x4 board and the goal is to create a consecutive 4 pegs in a row, column or diagonal.

###Rules:###
* Each player has 12 pegs in 4 different sizes ordered in stacks. The player can only place on the board the top peg on each stack.
* A player can move pegs that are already on the board in his turn.
* A player can cover his opponent peg with a bigger peg. While a peg is covered it cannot be moved. 
* It is not allowed to cover an opponent peg with a new peg unless this move will prevent a winning move.
* A player may uncovered his opponent peg in his turn but if a row, column or diagonal for his opponent by this move, the player lost the game.

Enjoy!


##Libraries in use
* Flask
* Jinja2
* MarkupSafe
* Werkzeug
* itsdangerous
* wsgiref
