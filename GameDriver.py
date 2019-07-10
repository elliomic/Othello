'''
    Erich Kramer - April 2017
    Apache License
    If using this code please cite creator.

	Modified May 2018 by Michael Elliott

'''
from Players import *
import sys
import OthelloBoard


class GameDriver:
    def __init__(self, p1type, p2type, num_rows, num_cols):
        if p1type.lower() in "human":
            self.p1 = HumanPlayer('X')

        elif p1type.lower() in "minimax" or p1type.lower() in "ai":
            self.p1 = MinimaxPlayer('X')

        else:
            print("Invalid player 1 type!")
            exit(-1)

        if p2type.lower() in "human":
            self.p2 = HumanPlayer('O')

        elif p2type.lower() in "minimax" or p2type.lower() in "ai":
            self.p2 = MinimaxPlayer('O')

        else:
            print("Invalid player 2 type!")
            exit(-1)

        self.board = OthelloBoard.OthelloBoard(num_rows, num_cols, self.p1.symbol, self.p2.symbol)
        self.board.initialize();

    def display(self):
        print("Player 1 (", self.p1.symbol, ") score: ", \
                self.board.count_score(self.p1.symbol))

    def process_move(self, curr_player, opponent):
        invalid_move = True
        while(invalid_move):
            (col, row) = curr_player.get_move(self.board)
            if( not self.board.is_legal_move(col, row, curr_player.symbol)):
                print("Invalid move")
            else:
                print("Move:", [col,row], "\n")
                self.board.play_move(col,row,curr_player.symbol)
                return;


    def run(self):
        current = self.p1
        opponent = self.p2
        self.board.display();

        toggle = False

        #main execution of game
        print("Player 1(", self.p1.symbol, ") move:")
        while True:
            if self.board.has_legal_moves_remaining(current.symbol):
                self.process_move(current, opponent);
                self.board.display()
            else:
                print("Can't move")
                break
            toggle = not toggle
            if not toggle:
                current, opponent = self.p1, self.p2
                print("Player 1(", self.p1.symbol, ") move:")
            else:
                current, opponent = self.p2, self.p1
                print("Player 2(", self.p2.symbol, ") move:")

        #decide win/lose/tie state
        state = self.board.count_score(self.p1.symbol) - self.board.count_score(self.p2.symbol)
        if( state == 0):
            print("Tie game!!")
        elif state >0:
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins!")
            


def main():
    if(len(sys.argv)) != 3:
        print("Usage:", sys.argv[0], "<player1 type> <player2 type>")
        exit(1)
    game = GameDriver(sys.argv[1], sys.argv[2], 4, 4)
    game.run();
    return 0
