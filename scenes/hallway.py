import pygame
from utils import *
import time

import random

CHAT_BOX_TOP = HEIGHT - HEIGHT / 3
CHAT_BOX_LEFT = 0

ANSWERS = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]

questions = {
    "martin" : [
        pygame.image.load("assets/images/coworkers/martin.png"),
        {
            "question" : "Si je suis bourré et qu'un moustique me pique, il fait un coma éthylique ?",
            "choices" : ["Oui", "Non", "Peut-être", "Je ne sais pas"],
            "answer" : [1, 0, 0, -1],
        },
        {
            "question" : "Si c'est mauvais de grignoter pendant la nuit, à quoi sert la lumière dans le frigo?",
            "choices" : ["Pour faire la fête avant de les manger", "Pour le monstre du frigo", "Pour te faire parler", "Je ne sais pas"],
            "answer" : [1,0,0 ,-1]
        },
        {
            "question" : "Pourquoi met on une pizza qui est ronde dans une boite carrée \n et la mange-t-on en forme de triangle ?",
            "choices" : ["Laisse moi tranquille", "Stp je suis occupé", "Demande à Pythagore", "Je ne sais pas"],
            "answer" : [1, 1, 1 , -1]
        },
    ], 
    "archibald" : [
        pygame.image.load("assets/images/coworkers/archibald.png"),
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
    "gabriel" : [
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
	#TODO BRUITS DE PAS
	# Set the zoom speed
	zoom_speed = 0.005
	scaled_image = bg
	score = 0
	for person in questions.values():
		# zoom_speed += 0.0001
		# Calculate the position to center the scaled image on the screen
		imititate_steps(scale_factor, zoom_speed, bg, display)
		score = render_talk(display, person, scaled_image)

		time.sleep(0.1)

		upd(clock, FPS)
		end()
	return score 

def imititate_steps(scale_factor, zoom_speed, bg, display):
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



def generate_chat_box(display : pygame.Surface, str: str, name, image : pygame.Surface, bg : pygame.Surface):
	"""
	Function to generate a chat box with a given string composed of multiple lines.
	"""
	generate_background_box(display, image, bg)
	text_general_offset = 10
	text_vertical_offset = 0
	# Load the fonts
	title_font = pygame.font.SysFont('Analogist.ttf', 40)
	font = pygame.font.SysFont('Analogist.ttf', 30)

	#Render the title
	title = title_font.render(name, True, Colors.YELLOW)
	text_vertical_offset += title.get_height() + 10
	display.blit(title, [text_general_offset, CHAT_BOX_TOP + text_general_offset])

	for line in str.splitlines():
		# # Render the text
		text = font.render(line, True, Colors.WHITE)
		display.blit(text, [text_general_offset, CHAT_BOX_TOP + text_general_offset + text_vertical_offset])
		text_vertical_offset += text.get_height()

def render_talk(display : pygame.Surface, Person_data : list, bg : pygame.Surface):
	"""
	Function to render a discussion between the player and a person.
	"""
	Score = 0
	generate_chat_box(display, Person_data[1]["question"], "Archibald", Person_data[0], bg)
	pygame.display.update()
	for i in range(1, len(Person_data)):
		generate_multiple_choice(display, Person_data[i]["choices"], Person_data[0], bg, Person_data[i]["question"])
		pygame.display.update()
		result = Person_data[i]["answer"][wait_for_input()]
		Score += result
		render_answer(display, result)
		pygame.display.update()
		time.sleep(0.2)
	return Score

def generate_background_box(display : pygame.Surface, image : pygame.Surface, bg : pygame.Surface):
	display.blit(bg, bg.get_rect(center=display.get_rect().center))
	Temporary_surface = pygame.Surface((WIDTH, HEIGHT), flags=pygame.SRCALPHA)
	border_color = (255, 255, 255, 255)
	center_color = (30, 30, 30, 170)  # Semi-transparent
	chat_box = pygame.Rect(0, CHAT_BOX_TOP, WIDTH, HEIGHT)
	pygame.draw.rect(Temporary_surface, center_color, chat_box, 0, 10)
	pygame.draw.rect(Temporary_surface, border_color, chat_box, 2, 10)
	display.blit(Temporary_surface, (0, 0))
	display.blit(image, (30, CHAT_BOX_TOP - image.get_height()))

def generate_multiple_choice(display : pygame.Surface, choices : list, image : pygame.Surface, bg : pygame.Surface, question : str):
	"""
	Function to generate a multiple choice box with a given list of choices.
	"""
	Line_spacing = 15
	generate_background_box(display, image, bg)
	# Load the fonts
	question_font = pygame.font.SysFont('Analogist.ttf', 30)
	answer_font = pygame.font.SysFont('Analogist.ttf', 25)

	question_text = question_font.render(question, True, Colors.YELLOW)
	display.blit(question_text, (Line_spacing, CHAT_BOX_TOP + Line_spacing))
	# #generate the 4 answer boxes
	for i, choice in enumerate(choices):
		# Render the text
		text = answer_font.render(str(i + 1) + ") " + choice, True, Colors.WHITE)
		# Draw the text
		display.blit(text, (Line_spacing, CHAT_BOX_TOP + Line_spacing + question_text.get_height() + Line_spacing + choices.index(choice) * 30))
	


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
		return
	border = pygame.Rect(0, 0, WIDTH, HEIGHT)
	pygame.draw.rect(Temporary_surface, border_color, border, 30, 10)
	display.blit(Temporary_surface, (0, 0))


