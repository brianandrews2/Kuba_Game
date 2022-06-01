# Author:  Brian Andrews
# Date:  06/05/2021
# Description:  The Kuba board game Class used by main.py
# Game rules are explained at this link:  https://sites.google.com/site/boardandpieces/list-of-games/kuba


class KubaGame:
    """
    Class representing the Kuba Board Game.  This class handles the initial setup of the board, all of the player
    movements including validation that each move is valid, get methods so the user can check on whose turn it is, who
    the winner is, how many marbles are captured, which marble is at a coordinate, and the number of each color marble
    left on the board.  Initial board setup indicates each row with either “B” for black marble, “W” for white marble,
    or “X” for empty space.  This class will not communicate with other classes.
    """

    def __init__(self, player_a, player_b):
        """
        Initiates the Kuba boards, player information, current turn to None and current winner to None.
        Main Board is the primary game board that the players interact with.
        Temp Board is used temporarily to check for the Ko rule to avoid making an illegal move on the main board.
        Prev Board is what Temp Board checks against to see if the move returns the board to the previous state which
        would violate the Ko rule.
        """

        self._row_0 = ["W", "W", "X", "X", "X", "B", "B"]
        self._row_1 = ["W", "W", "X", "R", "X", "B", "B"]
        self._row_2 = ["X", "X", "R", "R", "R", "X", "X"]
        self._row_3 = ["X", "R", "R", "R", "R", "R", "X"]
        self._row_4 = ["X", "X", "R", "R", "R", "X", "X"]
        self._row_5 = ["B", "B", "X", "R", "X", "W", "W"]
        self._row_6 = ["B", "B", "X", "X", "X", "W", "W"]
        self._player_a = player_a
        self._player_b = player_b
        self._player_a_captured = 0
        self._player_b_captured = 0
        self._player_a_color = player_a[1]
        self._player_b_color = player_b[1]
        self._player_a_name = player_a[0]
        self._player_b_name = player_b[0]
        self._current_turn = None
        self._winner = None

    def get_current_turn(self):
        """
        Returns the player whose turn it is.
        """
        return self._current_turn

    def make_move(self, player_name, coordinates, direction):
        """
        Takes a player name such as ("PlayerA"), coordinates such as (3, 5), and direction ("L" for left, "R" for right,
        "B" for backward, or "F" for forward) to move marbles for the players turn.  Validates that the move is legal
        and returns False if it is not legal.  After the turn is complete, if a marble was knocked off the marble and
        capture counts are updated.  If the game is won a winner is set.  If game is not won the current
        player is set to the next player, then the method returns True.
        """

        """determine first player to act"""
        if self._current_turn is None:
            self._current_turn = player_name

        """check if player is making a move after winner is decided"""
        if self._winner is not None:
            return False

        """check if player taking a turn during another player's turn to act"""
        if self._current_turn != player_name:
            return False

        """check for out of bounds coordinates"""
        x = coordinates[0]
        y = coordinates[1]
        if x < 0 or x > 6:
            return False
        if y < 0 or y > 6:
            return False

        """check for empty tile or wrong color tile"""
        selected_marble = self.get_marble(coordinates)
        if player_name == self._player_a_name:
            current_color = self._player_a_color
        if player_name == self._player_b_name:
            current_color = self._player_b_color
        if selected_marble != current_color:
            return False

        """determine which row to use for the movement"""
        if x == 0:
            current_row = self._row_0
        if x == 1:
            current_row = self._row_1
        if x == 2:
            current_row = self._row_2
        if x == 3:
            current_row = self._row_3
        if x == 4:
            current_row = self._row_4
        if x == 5:
            current_row = self._row_5
        if x == 6:
            current_row = self._row_6

        """check if movement direction is valid (L, R, B, F)"""
        if direction == "L":
            if y == 0:
                return False     #cannot push your own marble off

            if y != 6:
                adjacent_marble = self.get_marble((x, y+1))
                if adjacent_marble != "X":
                    return False

            """complete movement"""
            initialized_index = y
            index = y
            while index >= 0:
                if current_row[index] == "X":
                    """start pushing marbles"""
                    starting_index = index
                    for tiles in range(starting_index, initialized_index):
                        current_row[tiles] = current_row[tiles + 1]
                    current_row[initialized_index] = "X"

                    """set the turn order to the next player and return True"""
                    if player_name == self._player_a_name:
                        self._current_turn = self._player_b_name
                    if player_name == self._player_b_name:
                        self._current_turn = self._player_a_name
                    return True

                """push marble off"""
                if index == 0:
                    if current_row[0] == "R":
                        if self._current_turn == self._player_a_name:
                            self._player_a_captured += 1
                        if self._current_turn == self._player_b_name:
                            self._player_b_captured += 1
                    starting_index = index
                    for tiles in range(starting_index, initialized_index):
                        current_row[tiles] = current_row[tiles + 1]
                    current_row[initialized_index] = "X"

                    """set the turn order to the next player and return True"""
                    if player_name == self._player_a_name:
                        self._current_turn = self._player_b_name
                    if player_name == self._player_b_name:
                        self._current_turn = self._player_a_name
                    return True
                index -= 1

        if direction == "R":
            if y == 6:
                return False    #cannot push your own marble off

            if y != 0:
                adjacent_marble = self.get_marble((x, y-1))
                if adjacent_marble != "X":
                    return False

            """complete movement:"""
            initialized_index = y
            index = y
            while index <= 6:
                if current_row[index] == "X":
                    """start pushing marbles"""
                    starting_index = index
                    for tiles in range(starting_index, initialized_index, -1):
                        current_row[tiles] = current_row[tiles - 1]
                    current_row[initialized_index] = "X"

                    """set the turn order to the next player and return True"""
                    if player_name == self._player_a_name:
                        self._current_turn = self._player_b_name
                    if player_name == self._player_b_name:
                        self._current_turn = self._player_a_name
                    return True

                """push marble off"""
                if index == 6:
                    if current_row[6] == "R":
                        if self._current_turn == self._player_a_name:
                            self._player_a_captured += 1
                        if self._current_turn == self._player_b_name:
                            self._player_b_captured += 1
                    starting_index = index
                    for tiles in range(starting_index, initialized_index, -1):
                        current_row[tiles] = current_row[tiles - 1]
                    current_row[initialized_index] = "X"

                    """set the turn order to the next player and return True"""
                    if player_name == self._player_a_name:
                        self._current_turn = self._player_b_name
                    if player_name == self._player_b_name:
                        self._current_turn = self._player_a_name
                    return True
                index += 1

        if direction == "F":
            if x == 0:
                return False        #cannot push your own marble off

            row_list = [self._row_0, self._row_1, self._row_2, self._row_3, self._row_4, self._row_5, self._row_6]
            if x != 6:
                adjacent_marble = row_list[x+1][y]
                if adjacent_marble != "X":
                    return False

            """complete movement:"""
            initialized_index = x
            index = x
            while index >= 0:
                if row_list[index][y] == "X":
                    """start pushing marbles"""
                    starting_index = index
                    for tiles in range(starting_index, initialized_index):
                        row_list[tiles][y] = row_list[tiles + 1][y]
                    current_row[y] = "X"

                    """set the turn order to the next player and return True"""
                    if player_name == self._player_a_name:
                        self._current_turn = self._player_b_name
                    if player_name == self._player_b_name:
                        self._current_turn = self._player_a_name
                    return True

                """push marble off"""
                if index == 0:
                    if self._row_0[y] == "R":
                        if self._current_turn == self._player_a_name:
                            self._player_a_captured += 1
                        if self._current_turn == self._player_b_name:
                            self._player_b_captured += 1
                    starting_index = index
                    for tiles in range(starting_index, initialized_index):
                        row_list[tiles][y] = row_list[tiles + 1][y]
                    current_row[y] = "X"

                    """set the turn order to the next player and return True"""
                    if player_name == self._player_a_name:
                        self._current_turn = self._player_b_name
                    if player_name == self._player_b_name:
                        self._current_turn = self._player_a_name
                    return True
                index -= 1

        if direction == "B":
            if x == 6:
                return False    #cannot push your own marble off

            row_list = [self._row_0, self._row_1, self._row_2, self._row_3, self._row_4, self._row_5, self._row_6]
            if x != 0:
                adjacent_marble = row_list[x-1][y]
                if adjacent_marble != "X":
                    return False

            """complete movement:"""
            initialized_index = x
            index = x
            while index <= 6:
                if row_list[index][y] == "X":
                    """start pushing marbles"""
                    starting_index = index
                    for tiles in range(starting_index, initialized_index, -1):
                        row_list[tiles][y] = row_list[tiles - 1][y]
                    current_row[y] = "X"
                    """set the turn order to the next player and return True"""
                    if player_name == self._player_a_name:
                        self._current_turn = self._player_b_name
                    if player_name == self._player_b_name:
                        self._current_turn = self._player_a_name
                    return True

                """push marble off"""
                if index == 6:
                    if self._row_6[y] == "R":
                        if self._current_turn == self._player_a_name:
                            self._player_a_captured += 1
                        if self._current_turn == self._player_b_name:
                            self._player_b_captured += 1
                    starting_index = index
                    for tiles in range(starting_index, initialized_index, -1):
                        row_list[tiles][y] = row_list[tiles - 1][y]
                    current_row[y] = "X"

                    """set the turn order to the next player and return True"""
                    if player_name == self._player_a_name:
                        self._current_turn = self._player_b_name
                    if player_name == self._player_b_name:
                        self._current_turn = self._player_a_name
                    return True
                index += 1

        """set the turn order to the next player and return True"""
        if player_name == self._player_a_name:
            self._current_turn = self._player_b_name
        if player_name == self._player_b_name:
            self._current_turn = self._player_a_name

        """check for a winner"""
        if self._player_a_captured == 7:
            self._winner = self._player_a_name

        if self._player_b_captured == 7:
            self._winner = self._player_b_name

        marble_count = self.get_marble_count()
        white_count = marble_count[0]
        black_count = marble_count[2]
        if black_count == 0:
            if self._player_a_color == "B":
                self._winner = self._player_b_name
            if self._player_b_color == "B":
                self._winner = self._player_a_name
        if white_count == 0:
            if self._player_a_color == "W":
                self._winner = self._player_b_name
            if self._player_b_color == "W":
                self._winner = self._player_a_name
        return True

    def get_winner(self):
        """
        Returns the winner of the game if a winner has been chosen, or returns None if there is no winner yet.
        """
        return self._winner

    def get_captured(self, player):
        """
        Takes a player name as a parameter such as ("PlayerA") and returns the number of red marbles that player
        has captured.
        """
        if self._player_a_name == player:
            return self._player_a_captured

        if self._player_b_name == player:
            return self._player_b_captured

        else:
            return "Not a valid player name"

    def get_marble(self, coordinates):
        """
        Takes coordinates as a parameter such as (5, 6) and returns the color of marble at those coordinates or returns
         X if no marble is present.
        """
        x = coordinates[0]
        y = coordinates[1]
        if y < 0 or y > 6:
            return "Not a valid coordinate"
        if x < 0 or x > 6:
            return "Not a valid coordinate"
        if x == 0:
            return self._row_0[y]
        if x == 1:
            return self._row_1[y]
        if x == 2:
            return self._row_2[y]
        if x == 3:
            return self._row_3[y]
        if x == 4:
            return self._row_4[y]
        if x == 5:
            return self._row_5[y]
        if x == 6:
            return self._row_6[y]

    def get_marble_count(self):
        """
        Returns the number of white, black and red marbles as a tuple in the order (W,B,R).
        """
        white_count = 0
        black_count = 0
        red_count = 0
        for index in self._row_0:
            if index == "W":
                white_count += 1
            if index == "B":
                black_count += 1
            if index == "R":
                red_count += 1

        for index in self._row_1:
            if index == "W":
                white_count += 1
            if index == "B":
                black_count += 1
            if index == "R":
                red_count += 1

        for index in self._row_2:
            if index == "W":
                white_count += 1
            if index == "B":
                black_count += 1
            if index == "R":
                red_count += 1

        for index in self._row_3:
            if index == "W":
                white_count += 1
            if index == "B":
                black_count += 1
            if index == "R":
                red_count += 1

        for index in self._row_4:
            if index == "W":
                white_count += 1
            if index == "B":
                black_count += 1
            if index == "R":
                red_count += 1

        for index in self._row_5:
            if index == "W":
                white_count += 1
            if index == "B":
                black_count += 1
            if index == "R":
                red_count += 1

        for index in self._row_6:
            if index == "W":
                white_count += 1
            if index == "B":
                black_count += 1
            if index == "R":
                red_count += 1
        count_tuple = (white_count, black_count, red_count)
        return count_tuple

    def print_board(self):
        """
        Prints a visual of the game board
        """
        print(self._row_0)
        print(self._row_1)
        print(self._row_2)
        print(self._row_3)
        print(self._row_4)
        print(self._row_5)
        print(self._row_6)

    def get_player_a_color(self):
        """
        Returns the color of player A
        """
        return self._player_a_color

    def get_player_b_color(self):
        """
        Returns the color of player B
        """
        return self._player_b_color

    def get_player_a_name(self):
        """
        Returns the name of player A
        """
        return self._player_a_name

    def get_player_b_name(self):
        """
        Returns the name of player B
        """
        return self._player_b_name

    def get_player_a_count(self):
        """
        Returns the number of red marbles captured by player A
        """
        return self._player_a_captured

    def get_player_b_count(self):
        """
        Returns the number of red marbles captured by player B
        """
        return self._player_b_captured

def main():
    """
    Main function
    """
    pass

if __name__ == "__main__":
    main()
