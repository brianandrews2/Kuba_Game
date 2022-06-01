# Author:  Brian Andrews
# Date:  06/05/2021
# Description:  The Kuba board game main program that the user interacts with to play the game.

# Game rules below referenced from this link:  https://sites.google.com/site/boardandpieces/list-of-games/kuba

# Objective
#
# A player wins by pushing off and capturing seven neutral red stones or by pushing off all of the opposing stones.
# A player who has no legal moves available has lost the game.
#
# Play
#
# With alternating turns, players move a single marble in any orthogonal direction.  In order to slide a marble,
# however, there must be access to it.  For example, to slide a marble to the left, the cell just to the right if it
# must be vacant.  If there are other marbles; your own, your opponent's or the neutral red ones; in the direction of
# your move at the cell you are moving to, those marbles are pushed one cell forward along the axis of your move.
# Up to six marbles can be pushed by your one marble on your turn.  Although a player cannot push off one of his own
# marbles, any opposing counters that are pushed off are removed from the game and any neutral counters that are pushed
# off are captured by the pushing player to add to his or her store of captured neutral red marbles.  If you manage to
# push off a neutral or opposing marble, you are entitled to another turn.
# Kuba incorporates the Ko rule to prohibit the same position being repeated over and over again.

from KubaGame import KubaGame


def print_commands():
    """
    Prints the commands a user can enter during the game
    """
    print("")
    print("COMMANDS")
    print("board: Display the game board.")
    print("turn:  Display who's turn it is. (First turn displays None because either player can start first).")
    print("move:  Move player's marble.  The game will ask which marble and which direction as a follow up.")
    print("captured:  Displays how many red marbles each player has captured.")
    print("marble:  Display which color marble is at a location.  The game will ask which marble as a follow up.")
    print("count:  Display the count of each marble color on the board as (W,B,R).")
    print("colors: Display the marble color for each player.")
    print("names: Display the name of each player.")
    print("exit:  Quit the game.")
    print("")


def convert_coords(coords):
    """
    Converts coordinate string to integers
    """

    # verify coordinate length
    if len(coords) != 6:
        return False

    # verify that coordinates are each single digits, (10, 13) would be invalid
    check_string1 = coords[2:3]
    check_string2 = coords[5:6]
    if check_string1.isnumeric() or check_string2.isnumeric():
        return False

    # verify that each coordinate is a number
    if not coords[1:2].isnumeric():
        return False
    if not coords[4:5].isnumeric():
        return False

    coord1 = int(coords[1:2])
    coord2 = int(coords[4:5])

    # verify that each coordinate is between 0 and 6
    if coord1 > 6 or coord2 > 6:
        return False

    # verify coordinates are in parentheses
    if coords[0:1] != "(" or coords[5:6] != ")":
        return False

    new_coords = (coord1, coord2)
    return new_coords


def main():
    """
    Main program that user interacts with to set up the board and take each turn
    """

    # Player 1 setup
    player1_name = input("Enter player 1 name: ")
    player1_color = input("Enter capital B or W to select black or white marbles: ")

    # Invalid color selected
    if player1_color != "W" and player1_color != "B":
        player1_color = input("Invalid color.  Please select B or W marble color: ")

    # Player 2 setup
    player2_name = input("Enter player 2 name: ")
    if player1_color == "W":
        player2_color = "B"
    else:
        player2_color = "W"

    print("")
    print("Game board layout:  'B' and 'W' are player marbles, 'R' are the red marbles, 'X' are empty spaces.  ")
    print(f"{player1_name} is marble color '{player1_color}', "
          f"and {player2_name} is marble color '{player2_color}'.")
    print("To view possible commands, type 'commands' at any point.  Let the game begin!")
    print("")

    # Initialize board
    print("GAME BOARD")
    game = KubaGame((player1_name, player1_color), (player2_name, player2_color))
    game.print_board()
    print("")

    while True:
        # exit loop when winner is found
        if game.get_winner() is not None:
            winner = game.get_winner()
            print(f"{winner} is the winner!  Congratulations!")
            break

        # get command
        command = input("Enter command: ")

        # print commands
        if command == "commands":
            print_commands()

        # exit
        if command == "exit":
            break

        # print board
        if command == "board":
            print("")
            print("GAME BOARD")
            game.print_board()
            print("")

        # print who's turn it is
        if command == "turn":
            print(game.get_current_turn())

        # move a marble on the board
        if command == "move":

            # get player to move
            move_player = input("Which player is moving: ")

            # get coordinates to move from
            move_coords = input("Which marble coordinate, such as (0, 3), is being moved: ")
            int_coords = convert_coords(move_coords)
            if not int_coords:
                print("Invalid coordinates")
                continue

            # get direction to move
            move_direction = input("Which direction? Enter either R, L, U, or D for right, left, up, down: ")
            if move_direction != "R" and move_direction != "L" and move_direction != "U" and move_direction != "D":
                print("Invalid direction.  Must enter R, L, U or D.")
                continue

            # make the movement
            movement = game.make_move(move_player, int_coords, move_direction)
            if not movement:
                print("Invalid movement")
                continue

        # print how many marbles each player has captured
        if command == "captured":
            player1_captured = game.get_captured(player1_name)
            print(f"{player1_name} captured:  {player1_captured}")
            player2_captured = game.get_captured(player2_name)
            print(f"{player2_name} captured:  {player2_captured}")

        # print marble color at a location
        if command == "marble":
            marble_coords = input("Which marble coordinates, such as (2, 3), are you checking: ")
            int_coords = convert_coords(marble_coords)
            if not int_coords:
                print("Invalid coordinates")
                continue
            marble_color = game.get_marble(int_coords)
            print(f"The marble color at {marble_coords} is {marble_color}")

        # print how many of each marble are on the board
        if command == "count":
            marble_counts = game.get_marble_count()
            print(f"Marble counts (W, B, R) are {marble_counts}")

        # print which marble color each player is
        if command == "colors":
            print(f"{player1_name}'s marble color is {player1_color}")
            print(f"{player2_name}'s marble color is {player2_color}")

        # print the name of each player
        if command == "names":
            print(f"Player 1 name is {player1_name} and player 2 name is {player2_name}")


if __name__ == "__main__":
    main()
