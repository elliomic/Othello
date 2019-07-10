"""
Michael Elliott
CS 331
May 2018
"""

from Players import Player

class MinimaxPlayer(Player):
	def __init__(self, symbol):
		Player.__init__(self, symbol);
			
	def get_move(self, board):
		if self.symbol == 'X':
			(a, v) = max_value(board)
		else:
			(a, v) = min_value(board)
		return a

def successor_function(board, symbol):
	successors = list()
	# loop through each column
	for c in range(board.cols):
		# loop through each row
		for r in range(board.rows):
			# check if playing at each space is a legal move
			if board.is_legal_move(c, r, symbol):
				# create a clone of the board
				successor = board.cloneOBoard()
				# play the legal move on the board
				successor.play_move(c, r, symbol)
				# add the move and the resulting board to the list of successors
				successors.append(((c, r), successor))
	#return the list of successors
	return successors


def utility_function(board):
	# return the number of player 1 pieces minus the number of player 2 pieces
	return board.count_score(board.p1_symbol) - board.count_score(board.p2_symbol)

def max_value(state):
	# generate the successors for the given state
	successors = successor_function(state, state.p1_symbol)
	# check if there are no successors
	if not successors:
		# return the utility of the state
		return (None, utility_function(state))
	v = utility_function(state)
	a = successors[0][0]
	# loop through each successor
	for (sa, s) in successors:
		# get the min_value of the successor
		(ma, mv) = min_value(s)
		# check if the current value is less than the utility of the successor
		if v < mv:
			# set the value equal to the utility of the successor
			v = mv
			# set the action to the action that the successor resulted from
			a = sa
	# return the action and the utility of the action
	return (a, v)

def min_value(state):
	# generate the successors for the given state
	successors = successor_function(state, state.p2_symbol)
	# check if there are no successors
	if not successors:
		# return the utility of the state
		return (None, utility_function(state))
	v = utility_function(state)
	a = successors[0][0]
	# loop through each successor
	for (sa, s) in successors:
		# get the min_value of the successor
		(ma, mv) = max_value(s)
		# check if the current value is less than the utility of the successor
		if v > mv:
			# set the value equal to the utility of the successor
			v = mv
			# set the action to the action that the successor resulted from
			a = sa
	# return the action and the utility of the action
	return (a, v)
