"""
This is our main driver file. It will be responsible for handling user input and displaying the current GameState object.
"""

import pygame as p
from Chess import chessEngine

WIDTH = HEIGHT = 512 # 400, another good option
DIMENSION = 8 # dimension of the chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # for animations later on
IMAGES = {}

'''
Initialize a global dictionary of images.This will be called exactly once in the main
'''
def loadImages():
	pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
	for piece in pieces:
		IMAGES[piece] = p.transform.scale(p.image.pygame.image.load("images/" + piece +".png"))
	# Note: we can access an image by saying 'IMAGES['wp']'

'''
The main driver for our code.  This will handle user input and updating the graphics
'''
def main():
	p.init()
	screen = p.display.set_mode((WIDTH, HEIGHT))
	clock = p.time.Clock()
	screen.fill(p.Color("white"))
	gs = chessEngine.GameState()
	loadImages() # only do this once
	running = True
	while running:
		for e in p.event.get():
			if e.type == p.QUIT:
				running = False
		drawGameState(screen, gs)
		clock.tick(MAX_FPS)
		p.display.flip()
'''
Responsible for all graphics within a current GameStae
'''
def drawGameState(screen, gs):
	drawBoard(screen) # draw Squares on the Board
	# add in piece highlighting or move suggestions (later)
	drawPieces(screen, gs.board) # draw pieces on top of those squares
'''
Draw the squares on the board.
'''
def drawBoard(screen):
	colors = [p.Color("white"), p.Color("gray")]
	for r in range(DIMENSION):
		for c in range(DIMENSION):
			colors = colors[((r+c) % 2)]
			p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))



'''
draw pieces on the board using the current GameState.board
'''
def drawPieces(screen, board):
	pass





if __name__ == "__main__":
	main()