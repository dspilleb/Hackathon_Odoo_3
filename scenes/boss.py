from utils import *

import pygame

import time
from pprint import pprint


data = get_data()
pprint(data)

def activate(display: pygame.Surface, clock: pygame.time.Clock, FPS: int, total_score: int):
	"""
	\nFirst mini-game with the office and emails"""
	
	# load the background image
	bg = pygame.image.load('assets/images/desktop.png')
	bg = pygame.transform.smoothscale(bg, (WIDTH, HEIGHT))
	font = pygame.font.SysFont('Arial', 25)


	text = font.render(f"Vous avez atteint {total_score} point d'emplyé", True, Colors.BLACK)

	current = ""

	while 1:
		stop = False
		# when the user presses a key, check if it matches the current char
		# if it does, add the char to the current_mail
		# No more comment, code:

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				# enter
				if event.key == 13:
					stop = True
					break
				elif event.key == pygame.K_BACKSPACE:
					current = current[:-1]
				else: 
					current += event.unicode

			# display the text
			display.blit(bg, (0, 0))
			display.blit(text, (0, 0))
			name = font.render(current, True, Colors.BLACK)
			display.blit(name, (200,200))

			upd(clock, FPS)

		if stop:
			break
		
	name = current

	data[current] = total_score
	pprint(data)

	upd_data(data)

	# sort the data
	sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)

	# get the index of the current player
	index = sorted_data.index((name, total_score))


	msg1 = f"Merci Pour aujourd'hui {name}!"
	msg2 = f"Ton classement final est {index + 1}e sur {len(sorted_data)}"

	text = font.render(msg1, True, Colors.BLACK)
	text2 = font.render(msg2, True, Colors.BLACK)

	display.blit(bg, (0, 0))
	display.blit(text, (200,200))
	display.blit(text2, (200,250))


	upd(clock, FPS)
	
	while 1 :
		end()

