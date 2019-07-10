'''
    Erich Kramer - April 2017
    Apache License
    If using this code please cite creator.

'''

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    #PYTHON: use obj.symbol instead
    def get_symbol(self):
        return self.symbol
    
    #parent get_move should not be called
    def get_move(self, board):
        raise NotImplementedError()



class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol);

    def clone(self):
        return HumanPlayer(self.symbol)
        
	#PYTHON: return tuple instead of change reference as in C++
    def get_move(self, board):
        row = int(input("Enter row:"))
        col = int(input("Enter col:"))
        return  (col, row)

from MinimaxPlayer import *
