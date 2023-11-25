from utils import *

import pygame

# activate shows the bg_filler.png images and the scrolling text

def activate(display: pygame.Surface, clock: pygame.time.Clock, FPS: int):
	"""
	\nFunction to play the context of the game"""
	# scrolling text to explain the game over odoo promotional background music

	# load the background image
	bg = pygame.image.load('assets/images/bg_filler.png')
	# use Arial font
	font = pygame.font.SysFont('Arial', 25)
	# create the text cented horizontally
	text = font.render('This is the context of the game', True, Colors.WHITE)
	

	# scroll the text from up to down

	for i in range(HEIGHT//3):
		# blit dessine l'élément text aux coords 0,i
		display.blit(bg, (0, 0))
		display.blit(text, (0, i*3))
		upd(clock, FPS)
		end()

	return