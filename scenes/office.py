from utils import *

import pygame
import os

import datetime as dt
import time
import random

TEXT_TO_WRITE_POSX = 40
TEXT_TO_WRITE_POSY = 250

QUESTION_TO_WRITE_POSX = 40
QUESTION_TO_WRITE_POSY = 250

SCREEN_TOP_COORDS = (160, 80)
SCREEN_BOT_COORDS = (590, 310)

SCREEN_WIDTH = SCREEN_BOT_COORDS[0] - SCREEN_TOP_COORDS[0]
SCREEN_HEIGHT = SCREEN_BOT_COORDS[1] - SCREEN_TOP_COORDS[1]

COMPUTER_SPRITE = pygame.image.load('assets/images/Computer mainscreen.jpg')
COMPUTER_SPRITE = pygame.transform.smoothscale(COMPUTER_SPRITE, (SCREEN_BOT_COORDS[0] - SCREEN_TOP_COORDS[0], SCREEN_BOT_COORDS[1] - SCREEN_TOP_COORDS[1]))
COMPUTER_SPRITE.set_alpha(48)

MAIL_SCREEN_SPRITE = pygame.image.load('assets/images/Mail.png')
MAIL_SCREEN_SPRITE = pygame.transform.smoothscale(MAIL_SCREEN_SPRITE, (WIDTH, HEIGHT))


DESKTOP_SPRITE = pygame.image.load('assets/images/desktop.png')
DESKTOP_SPRITE = pygame.transform.smoothscale(DESKTOP_SPRITE, (WIDTH, HEIGHT))

NOTIFICATION_SPRITE = pygame.image.load('assets/images/notification.png')
NOTIFICATION_SPRITE = pygame.transform.smoothscale_by(NOTIFICATION_SPRITE, 0.2)

MESSAGE_SPRITE = pygame.image.load('assets/images/Message.png')
MESSAGE_SPRITE = pygame.transform.smoothscale_by(MESSAGE_SPRITE, 0.5)

QUESTION_SPRITE = pygame.image.load('assets/images/Question_message.png')
QUESTION_SPRITE = pygame.transform.smoothscale_by(QUESTION_SPRITE, 0.7)


PERSONS_SPRITES = [pygame.image.load('assets/images/Persons/homme.png'), pygame.image.load('assets/images/Persons/homme2.png'), pygame.image.load('assets/images/Persons/femme.png'), pygame.image.load('assets/images/Persons/femme2.png')]
PERSONS_SPRITES = [pygame.transform.smoothscale_by(sprite, 0.1) for sprite in PERSONS_SPRITES]

NOTIFICATION_PHONE_SPRITE = pygame.image.load('assets/images/notification_tel.png')
NOTIFICATION_PHONE_SPRITE = pygame.transform.smoothscale_by(NOTIFICATION_PHONE_SPRITE, 0.05)

#Sons
office_sound = "assets/sons/office_sound.mp3"
notification_sound = "assets/sons/notification_sound.wav"

emails = [
	"Salut Florence! J'ai oublié mon code, tu peux me l'envoyer?",
	"Je ne sais pas quoi offrir comme cadeau à Florent, tu as des idées?",
	"T'as vu?! Lou est enfin passée badge argent sur Phished.io!"
]

questions = [
	{
		"Question": "Qui aime le chocolat le plus ? J'ai oublié...",
		"Answer": "Lou"
	},
	{
		"Question": "C'est quoi le code de Florence stp ?",
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
	font = pygame.font.Font('assets/Roboto-Medium.ttf', 20)
	font_mail = pygame.font.SysFont('Arial', 25)
	bg = DESKTOP_SPRITE
	times = []

	if os.path.exists(office_sound):
		son = pygame.mixer.Sound(office_sound)
		son.play(-1)
	for email, Q in zip(emails, questions):

		bg = change_desk_to_mail_screen(display, clock, FPS)
		to_type = font_mail.render(email, True, (128, 128, 128))

		current_mail = ""
		start = dt.datetime.now()
		for char in email:
			while 1:
				stop = False
				# when the user presses a key, check if it matches the current char
				# if it does, add the char to the current_mail
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.unicode == char:
							current_mail += char
							stop = True
							break

					display.blit(bg, (0, 0))
					display.blit(to_type, (TEXT_TO_WRITE_POSX, TEXT_TO_WRITE_POSY))
					text = font_mail.render(current_mail, True, Colors.BLACK)
					display.blit(text, (TEXT_TO_WRITE_POSX,TEXT_TO_WRITE_POSY))
					if time.time() % 1 > 0.5:
						typing_bar(display, font_mail, current_mail)
					upd(clock, FPS)
					
				if stop:
					break

		times.append((dt.datetime.now() - start).total_seconds())

		question = Q["Question"]
		answer = Q["Answer"]
		question = font.render(question, True, Colors.BLACK)

		current = ""

		start = dt.datetime.now()
		change_desk_to_question_screen(display, clock, FPS)
		phone_question(display, question)
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

				render_answer(display, current, font)
				pygame.display.update()

			if stop:
				break

		times.append((dt.datetime.now() - start).total_seconds())

	pygame.mixer.stop()
	return 1000 - sum(times)*3

def typing_bar(display : pygame.Surface, current_font : pygame.font.Font, current_mail : str):
	typing_bar = current_font.render("|", True, (70, 70, 70))
	display.blit(typing_bar, (TEXT_TO_WRITE_POSX + current_font.render(current_mail, True, Colors.BLACK).get_width(),TEXT_TO_WRITE_POSY))
	pygame.display.update()
	return


def change_desk_to_mail_screen(display : pygame.Surface, clock : pygame.time.Clock, FPS : int):
	"""
	Function to change the screen to the mail screen if the user clicks on the screen
	"""
	display.blit(DESKTOP_SPRITE, (0, 0))
	display.blit(COMPUTER_SPRITE, (SCREEN_TOP_COORDS[0], SCREEN_TOP_COORDS[1]))
	bg = display.copy()
	pygame.display.update()
	time.sleep(random.randint(1, 5))
	#afficher une notification
	if os.path.exists(notification_sound):
		son = pygame.mixer.Sound(notification_sound)
		son.play()
	pop_image(display, NOTIFICATION_SPRITE, SCREEN_TOP_COORDS[0], SCREEN_TOP_COORDS[1])
	pygame.display.update()
	time.sleep(0.5)
	return MAIL_SCREEN_SPRITE

#TODO METTRE UNE NOTIF SUR LE TEL

def change_desk_to_question_screen(display : pygame.Surface, clock : pygame.time.Clock, FPS : int):
	"""
	Function to change the screen to the mail screen if the user clicks on the screen
	"""
	display.blit(DESKTOP_SPRITE, (0, 0))
	display.blit(COMPUTER_SPRITE, (SCREEN_TOP_COORDS[0], SCREEN_TOP_COORDS[1]))
	bg = display.copy()
	pygame.display.update()
	time.sleep(random.randint(1, 2))
	#afficher une notification
	if os.path.exists(notification_sound):
		son = pygame.mixer.Sound(notification_sound)
		son.play()
	pop_image(display, NOTIFICATION_PHONE_SPRITE, WIDTH - 295, HEIGHT - 310)
	pygame.display.update()
	time.sleep(0.5)
	return display

def phone_question(display : pygame.Surface, question : pygame.Surface):
	display.blit(QUESTION_SPRITE, (WIDTH - QUESTION_SPRITE.get_width(), HEIGHT - 365))
	pop_image(display, PERSONS_SPRITES[random.randint(0, 3)], WIDTH - QUESTION_SPRITE.get_width() + 30, HEIGHT - 100)
	display.blit(question, (WIDTH - QUESTION_SPRITE.get_width() + 35, HEIGHT - 50))
	pygame.display.update()
	time.sleep(2)

def render_answer(display : pygame.Surface, string : str, font : pygame.font.Font):
	display.blit(pygame.transform.flip(MESSAGE_SPRITE, True, False), (SCREEN_TOP_COORDS[0], SCREEN_BOT_COORDS[1] - MESSAGE_SPRITE.get_height()))
	text = font.render(string, True, Colors.WHITE)
	display.blit(text, (SCREEN_TOP_COORDS[0] + 40 ,SCREEN_BOT_COORDS[1] - 75))

# def render_call_from_boos(display : pygame.Surface