import pygame
from utils import *
import time
import os
import random

CHAT_BOX_TOP = HEIGHT - HEIGHT / 3
CHAT_BOX_LEFT = 0
text_general_offset = 10

ANSWERS = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]

questions = {
    "Martin" : [
        pygame.image.load("assets/images/coworkers/martin.png"),
        {
            "question" : "Si je suis bourré et qu'un moustique me pique, il fait un coma éthylique ?",
            "choices" : ["Oui", "Non", "Peut-être", "Je ne sais pas"],
            "answer" : [1, 0, 0, -1],
        },
        {
            "question" : "Si c'est mauvais de grignoter pendant la nuit, à quoi sert la lumière dans le frigo?",
            "choices" : ["Pour que les légumes fassent la fête avant de les manger", "Pour le monstre du frigo", "Pour te faire parler", "Je ne sais pas"],
            "answer" : [1,0,0 ,-1]
        },
        {
            "question" : "Pourquoi met on une pizza qui est ronde dans une boite carrée \n et la mange-t-on en forme de triangle ?",
            "choices" : ["Laisse moi tranquille", "Stp je suis occupé", "Demande à Pythagore", "Je ne sais pas"],
            "answer" : [1, 1, 1 , -1]
        },
    ], 
    "Archibald" : [
        pygame.transform.smoothscale_by(pygame.image.load("assets/images/coworkers/archibald.png"), 0.7),
        {
            "question" : "Ta cravate est trop moche",
            "choices" : ["Je sais", "La tienne aussi", "J'ai pas de cravate aujourd'hui", "T'as la même"],
            "answer" : [0, -1, 1, 1], 
        },
        {
            "question" : "Fait moi un café",
            "choices" : ["Non dsl", "Oui maitre", "*jette ton café dessus*", "Je ne bois pas de café"],
            "answer" : [0, 1, -1, 0]
        }, 
        {
            "question" : "Ils engagent vraiment n'importe qui ici",
            "choices" : ["Bah ouais tu tu t'es fait engager", "Normal t'a vu le QI de Martin?", "Désolé je démissionne", "Je suis là pour changer ça"],
            "answer" : [-1, -1, 0, 1]
        }
    ], 
    "Gabriel" : [
        pygame.image.load("assets/images/coworkers/gabriel.png"),
        {
            "question" : "Yo! Tu veux faire des heures supp' avec moi ce week-end ?",
            "choices" : ["Déso je joue à LOL", "Je suis pas là ce week-end", "Je suis pas payé pour ça", "Je suis pas ton pote"],
            "answer" : [-2, 1, 0, -1]
        },
        {
            "question" : "J'ai vraiment besoin de parler à quelqu'un...",
            "choices" : ["Je ne suis pas psy", "Bien sûr plus tard", "Me dérange pas je travaille", "Je suis pas ton pote"],
            "answer" : [0, 1, -1, -1]
        },
        {
            "question" : "Ah et tu veux bien me prêter 10€ pour un café?",
            "choices" : ["Bah non", "Tu me rends la monnaie?", "Prend moi en un aussi!", "Je suis pas ton pote"],
            "answer" : [-1, 0, 1, -1]
        }
    ],
}
shoes_sound = "assets/sons/chaussures.wav"
archibald_sound = "assets/sons/mr_bean_hello.mp3"
gabriel_sound = "assets/sons/yo.wav"
martin_sound = "assets/sons/heehee_sound.mp3"

def name_sound(name):
	print("bonjour")
	if name == "Martin":
		if os.path.exists(martin_sound):
			son = pygame.mixer.Sound(martin_sound)
			son.play()
	elif name == "Archibald":
		if os.path.exists(archibald_sound):
			son = pygame.mixer.Sound(archibald_sound)
			son.play()
	elif name == "Gabriel":
		if os.path.exists(gabriel_sound):
			son = pygame.mixer.Sound(gabriel_sound)
			son.play()  

def activate(display: pygame.Surface, clock: pygame.time.Clock, FPS: int):

	# Load the background
	bg = pygame.image.load("assets/images/hallway.png")
	bg = pygame.transform.smoothscale(bg, (WIDTH, HEIGHT))
	bg_rect = bg.get_rect()

	#Image to darken
	dark = pygame.Surface((WIDTH, HEIGHT), flags=pygame.SRCALPHA)
	dark.fill((30, 30, 30, 0))
	bg.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
	# Set the initial scale factor
	scale_factor = 1
	# Set the zoom speed
	zoom_speed = 0.005
	scaled_image = bg
	score = 0
	for name, person in questions.items():
		# zoom_speed += 0.0001
		# Calculate the position to center the scaled image on the screen
		imititate_steps(scale_factor, zoom_speed, bg, display)
		score = render_talk(display, person, scaled_image, name)

		time.sleep(0.1)

		upd(clock, FPS)
		end()
	return score 

def imititate_steps(scale_factor, zoom_speed, bg, display):
	if os.path.exists(shoes_sound):
		son = pygame.mixer.Sound(shoes_sound)
		son.play()
	for i in range(20):
		if (scale_factor < 1.5):
			# Increase the scale factor
			scale_factor += zoom_speed
			# Scale the image
			scaled_image = pygame.transform.smoothscale_by(bg, scale_factor)
			image_pos = scaled_image.get_rect(center=display.get_rect().center)
			display.blit(scaled_image, image_pos)
			pygame.display.update()
			time.sleep(0.1)
	pygame.mixer.stop()

def render_talk(display : pygame.Surface, Person_data : list, bg : pygame.Surface, name : str):
	"""
	Function to render a discussion between the player and a person.
	"""
	name_sound(name)
	Score = 0
	generate_background_box(display, Person_data[0], bg, name)
	pygame.display.update()
	for i in range(1, len(Person_data)):
		generate_multiple_choice(display, Person_data[i]["choices"], Person_data[0], bg, Person_data[i]["question"], name)
		pygame.display.update()
		result = Person_data[i]["answer"][wait_for_input()]
		Score += result
		render_answer(display, result)
		pygame.display.update()
		time.sleep(0.2)
	return Score

def generate_background_box(display : pygame.Surface, image : pygame.Surface, bg : pygame.Surface, name : str):
	title_font = pygame.font.Font('assets/Angels.ttf', 70)
	display.blit(bg, bg.get_rect(center=display.get_rect().center))
	Temporary_surface = pygame.Surface((WIDTH, HEIGHT), flags=pygame.SRCALPHA)
	border_color = (255, 255, 255, 255)
	center_color = (30, 30, 30, 170)  # Semi-transparent
	chat_box = pygame.Rect(0, CHAT_BOX_TOP, WIDTH, HEIGHT)
	pygame.draw.rect(Temporary_surface, center_color, chat_box, 0, 10)
	pygame.draw.rect(Temporary_surface, border_color, chat_box, 2, 10)
	display.blit(Temporary_surface, (0, 0))
	display.blit(image, (30, CHAT_BOX_TOP - image.get_height()))
	#Render the Name
	title = title_font.render(name, True, Colors.YELLOW)
	display.blit(title, [image.get_width() + (text_general_offset * 4), CHAT_BOX_TOP - image.get_height() / 2])

def generate_multiple_choice(display : pygame.Surface, choices : list, image : pygame.Surface, bg : pygame.Surface, question : str, name : str):
	"""
	Function to generate a multiple choice box with a given list of choices.
	"""
	Line_spacing = 10
	generate_background_box(display, image, bg, name)
	# Load the fonts
	question_font = pygame.font.SysFont('Analogist.ttf', 30)
	answer_font = pygame.font.SysFont('Analogist.ttf', 25)
	text_vertical_offset = 0

	question_text = ""
	for line in question.split("\n"):
		question_text = question_font.render(line, True, Colors.YELLOW)
		display.blit(question_text, (Line_spacing, CHAT_BOX_TOP + Line_spacing + text_vertical_offset))
		text_vertical_offset += question_text.get_height()
	# #generate the 4 answer boxes
	for i, choice in enumerate(choices):
		# Render the text
		text = answer_font.render(str(i + 1) + ") " + choice, True, Colors.WHITE)
		# Draw the text
		display.blit(text, (Line_spacing, CHAT_BOX_TOP + Line_spacing + question_text.get_height() + Line_spacing + choices.index(choice) * 25 + text_vertical_offset))
	


def wait_for_input():
	"""
	Function to wait for the user to press a key.
	"""
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key in ANSWERS:
					return (ANSWERS.index(event.key))
			elif event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

def render_answer(display : pygame.Surface, answer : int):
	Temporary_surface = pygame.Surface((WIDTH, HEIGHT), flags=pygame.SRCALPHA)
	if (answer > 0):
		border_color = (0, 255, 0, 30)
	elif (answer < 0):
		border_color = (255, 0, 0, 30)
	else:
		border_color = (255, 255, 0, 30)
	border = pygame.Rect(0, 0, WIDTH, HEIGHT)
	pygame.draw.rect(Temporary_surface, border_color, border, 30, 10)
	display.blit(Temporary_surface, (0, 0))


