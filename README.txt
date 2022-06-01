# Kuba Game
# To play this game, save the KubaGame.py class and main.py in the same directory.  In the terminal, execute main.py.  The game will request inputs for player names, which marble color they want, and then the game will begin.

Example:

Enter player 1 name: John
Enter capital B or W to select black or white marbles: W
Enter player 2 name: Smith

Game board layout:  'B' and 'W' are player marbles, 'R' are the red marbles, 'X' are empty spaces.
John is marble color 'W', and Smith is marble color 'B'.
To view possible commands, type 'commands' at any point.  Let the game begin!

GAME BOARD
['W', 'W', 'X', 'X', 'X', 'B', 'B']
['W', 'W', 'X', 'R', 'X', 'B', 'B']
['X', 'X', 'R', 'R', 'R', 'X', 'X']
['X', 'R', 'R', 'R', 'R', 'R', 'X']
['X', 'X', 'R', 'R', 'R', 'X', 'X']
['B', 'B', 'X', 'R', 'X', 'W', 'W']
['B', 'B', 'X', 'X', 'X', 'W', 'W']

Enter command: commands

COMMANDS
board: Display the game board.
turn:  Display who's turn it is. (First turn displays None because either player can start first).
move:  Move player's marble.  The game will ask which marble and which direction as a follow up.
captured:  Displays how many red marbles each player has captured.
marble:  Display which color marble is at a location.  The game will ask which marble as a follow up.
count:  Display the count of each marble color on the board as (W,B,R).
colors: Display the marble color for each player.
names: Display the name of each player.
exit:  Quit the game.

Enter command: move
Which player is moving: John
Which marble coordinate, such as (0, 3), is being moved: (0, 0)
Which direction? Enter either R, L, U, or D for right, left, up, down: R
Enter command: board

GAME BOARD
['X', 'W', 'W', 'X', 'X', 'B', 'B']
['W', 'W', 'X', 'R', 'X', 'B', 'B']
['X', 'X', 'R', 'R', 'R', 'X', 'X']
['X', 'R', 'R', 'R', 'R', 'R', 'X']
['X', 'X', 'R', 'R', 'R', 'X', 'X']
['B', 'B', 'X', 'R', 'X', 'W', 'W']
['B', 'B', 'X', 'X', 'X', 'W', 'W']

Enter command: turn
Smith
Enter command: