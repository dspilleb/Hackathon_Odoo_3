from utils import *

import pygame

import datetime as dt

emails = [
	"Salut Florence! J'ai oubliée mon code, tu peux me l'envoyer?",
	"Je ne sais pas quoi offrir comme cadeau à Florent, tu as des idées?",
	"T'as vu?! Lou est enfin passée badge argent sur Phished.io!"
]

questions = [
	{
		"Question": "Qui aime le chocolat le plus?",
		"Answer": "Lou"
	},
	{
		"Question": "C'est quoi le code de Florence?",
		"Answer": "5168451213568978155"
	},
	{
		"Question": "C'est possible d'être embauché à Odoo sans cv?",
		"Answer": "oui"
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

		to_type = font.render(email, True, Colors.BLACK)

		current_mail = ""
		start = dt.datetime.now()
		for char in email:
			while 1:
				stop = False
				# when the user presses a key, check if it matches the current char
				# if it does, add the char to the current_mail
				# No more comment, code:

				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.unicode == char:
							current_mail += char
							print(current_mail)
							stop = True
							break

					# display the text
					display.blit(bg, (0, 0))
					display.blit(to_type, (0, 0))
					text = font.render(current_mail, True, Colors.BLACK)
					display.blit(text, (200,200))
		
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
