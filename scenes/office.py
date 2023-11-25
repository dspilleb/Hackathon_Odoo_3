from utils import *

import pygame

import datetime as dt
import time

TEXT_TO_WRITE_POSX = 200
TEXT_TO_WRITE_POSY = 200

SCREEN_TOP_COORDS = (160, 80)
SCREEN_BOT_COORDS = (590, 310)

SCREEN_WIDTH = SCREEN_BOT_COORDS[0] - SCREEN_TOP_COORDS[0]
SCREEN_HEIGHT = SCREEN_BOT_COORDS[1] - SCREEN_TOP_COORDS[1]

COMPUTER_SPRITE = pygame.image.load('assets/images/Computer mainscreen.jpg')
COMPUTER_SPRITE = pygame.transform.smoothscale(COMPUTER_SPRITE, (SCREEN_BOT_COORDS[0] - SCREEN_TOP_COORDS[0], SCREEN_BOT_COORDS[1] - SCREEN_TOP_COORDS[1]))
COMPUTER_SPRITE.set_alpha(48)

emails = [
	"Bonjour, voici le premier email à Traiter",
]

questions = [
	{
		"Question": "Qui aime le chocolat le plus?",
		"Answer": "Lou"
	}, 
]


def activate(display: pygame.Surface, clock: pygame.time.Clock, FPS: int):
	"""
	\nFirst mini-game with the office and emails"""
	
	# load the background image
	bg = pygame.image.load('assets/images/desktop.png')
	bg = pygame.transform.smoothscale(bg, (WIDTH, HEIGHT))
	font = pygame.font.SysFont('Arial', 25)

	times = []

	for email in emails:

		to_type = font.render(email, True, (128, 128, 128))

		current_mail = ""
		start = dt.datetime.now()
		for char in email:
			while 1:
				stop = False
				# when the user presses a key, check if it matches the current char
				# if it does, add the char to the current_mail
				# No more comment, code:ù
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.unicode == char:
							current_mail += char
							stop = True
							break
				# display the text
					# display the text
					display.blit(bg, (0, 0))
					display.blit(COMPUTER_SPRITE, (SCREEN_TOP_COORDS[0], SCREEN_TOP_COORDS[1]))
					display.blit(to_type, (TEXT_TO_WRITE_POSX, TEXT_TO_WRITE_POSY))
					text = font.render(current_mail, True, Colors.BLACK)
					display.blit(text, (200,200))
					typing_bar(display, font, current_mail)
					# Mail_box(display, email)
					upd(clock, FPS)
					
				if stop:
					break

		times.append((dt.datetime.now() - start).total_seconds())

	for Q in questions:
		question = Q["Question"]
		answer = Q["Answer"]

		question = font.render(question, True, Colors.BLACK)

		current = ""

		start = dt.datetime.now()
		while 1:
			stop = False
			# when the user presses a key, check if it matches the current char
			# if it does, add the char to the current_mail
			# No more comment, code:

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE:
						current = current[:-1]

						if current.lower() == answer.lower():
							stop = True
							break
					else: 
						current += event.unicode

						if current.lower() == answer.lower():
							stop = True
							break

				# display the text
				display.blit(bg, (0, 0))
				display.blit(question, (0, 0))
				text = font.render(current, True, Colors.BLACK)
				display.blit(text, (200,200))
				upd(clock, FPS)

			if stop:
				break

		times.append((dt.datetime.now() - start).total_seconds())

	return 1000 - sum(times)*3

	print(times)

def typing_bar(display : pygame.Surface, current_font : pygame.font.Font, current_mail : str):
	typing_bar = current_font.render("|", True, Colors.BLACK)
	display.blit(typing_bar, (200 + current_font.render(current_mail, True, Colors.BLACK).get_width(),200))
	pygame.display.update()
	return

# def Mail_box(display : pygame.Surface, mail : str):
# 	pygame.draw.rect(display, Colors.BLACK, (0, 0, 200, 400), 0, 10)
# 	pygame.draw.rect(display, Colors.WHITE, (0, 0, 200, 400), 2, 10)
# 	pygame.display.update()
# 	return