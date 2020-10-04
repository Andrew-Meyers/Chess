"""
This class will be reponsible for storing all the imformation about the current state of a chess game.  It will also be
responsible for determinig valid moves at the current state. It will also keep a move log
"""
class GameState():
	def __init__(self):
		# Board is an 8x8 2d list, each element of the list has 2 characters,
		# The first character represents the color of piece, 'b' or 'w'
		# The second character represents the type of the piece, 'K', 'Q', 'R', 'B', 'N' or 'P'
		# "--" represents an empty space with no piece
		self.board = [
			["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
			["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
			["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
		self.whiteToMove = True
		self.moveLog = []