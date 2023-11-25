import pygame

import sys


FPS = 30
HEIGHT = 400
WIDTH = 600


class Colors:
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	BLUE = (0, 0, 255)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	


def upd(clock: pygame.time.Clock, frames_per_second: int):
	"""
	\nFunction to update the display and tick the clock.
	"""
	pygame.display.flip()
	clock.tick(frames_per_second)


def end():
	"""
	\nFunction to add at the end of every scene.
	\nEnds the game and quits pygame when the users closes the window.
	"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
