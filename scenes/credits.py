
from utils import *

import pygame


def activate(display: pygame.Surface, clock: pygame.time.Clock, FPS: int):

	florence = pygame.image.load('assets/images/coachs/florence.png')
	florence = pygame.transform.smoothscale_by(florence, 0.16)

	florent = pygame.image.load('assets/images/coachs/florent.png')
	florent = pygame.transform.smoothscale_by(florent, 0.16)

	lou = pygame.image.load('assets/images/coachs/lou.png')
	lou = pygame.transform.smoothscale_by(lou, 0.16)

	nathan = pygame.image.load('assets/images/coachs/nathan.png')
	nathan = pygame.transform.smoothscale_by(nathan, 0.16)

	nicolas = pygame.image.load('assets/images/coachs/nicolas.png')
	nicolas = pygame.transform.smoothscale_by(nicolas, 0.16)

	font = pygame.font.SysFont('Algerian', 35)

	txt_florence = font.render("Merci à Florence", True, Colors.BLACK)
	txt_florent = font.render("Merci à Florent", True, Colors.BLACK)
	txt_lou = font.render("Merci à Lou", True, Colors.BLACK)
	txt_nathan = font.render("Merci à Nathan", True, Colors.BLACK)
	txt_nicolas = font.render("Merci à Nicolas", True, Colors.BLACK)

	# load applauds.mp3
	pygame.mixer.music.load('assets/sons/applauds.mp3')

	# loop it
	pygame.mixer.music.play(-1)



	# add all objects and scroll them through the screen

	for i in range(HEIGHT*3):
		display.fill(Colors.WHITE)

		display.blit(lou, (WIDTH//4, HEIGHT*3 + 25 - i-HEIGHT*3))
		display.blit(txt_lou, (WIDTH//4, HEIGHT*3 + 25 -   i-HEIGHT*3))

		display.blit(florence, (0, HEIGHT*3 -  i-HEIGHT*2))
		display.blit(txt_florence, (0, HEIGHT*3 -  i-HEIGHT*2))

		display.blit(florent, (WIDTH//2, HEIGHT*3 -  i-HEIGHT*2))
		display.blit(txt_florent, (WIDTH//2, HEIGHT*3 -  i-HEIGHT*2))

		display.blit(nicolas, (0, HEIGHT*3 -  i-HEIGHT))
		display.blit(txt_nicolas, (0, HEIGHT*3 -  i-HEIGHT))

		display.blit(nathan, (WIDTH//2, HEIGHT*3 -  i-HEIGHT))
		display.blit(txt_nathan, (WIDTH//2, HEIGHT*3 -  i-HEIGHT))

		# display.blit(florence, (0, i))
		# display.blit(txt_florence, (0, i+10))

		# display.blit(florent, (WIDTH//2, i))
		# display.blit(txt_florent, (WIDTH//2, i+10))

		# display.blit(nathan, (0, i-HEIGHT))
		# display.blit(txt_nathan, (0, i-HEIGHT+10))

		# display.blit(nicolas, (WIDTH//2, i-HEIGHT))
		# display.blit(txt_nicolas, (WIDTH//2, i-HEIGHT+10))

		# display.blit(lou, (0, i-HEIGHT*2))
		# display.blit(txt_lou, (WIDTH//2, i-HEIGHT*2+10))

		upd(clock, FPS)
		end()
