from utils import *

import pygame

#!! so far this just waits for a click
def activate(display: pygame.Surface, clock: pygame.time.Clock, FPS: int):
	"""
	\nFirst mini-game with the office and emails"""
	
	# load the background image
	bg = pygame.image.load('assets/images/bureau.png')

	while 1:
		display.blit(bg, (0, 0))
		upd(clock, FPS)
		# does nothing until click returns the function
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				return
		
			end()
		end()
