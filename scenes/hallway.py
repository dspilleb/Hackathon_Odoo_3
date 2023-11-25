import pygame
from utils import *
import time

import random

CHAT_BOX_TOP = CHAT_BOX_TOP
CHAT_BOX_LEFT = 0

questions = {
    "martin" : [
        pygame.transform.smoothscale_by(pygame.image.load("assets/images/coworkers/martin.png"), 0.7),
        {
            "question" : "Si je suis bourré et qu'un moustique me pique, il fait un coma éthylique ?",
            "choices" : ["Oui", "Non", "Peut-être", "Je ne sais pas"],
            "scoring" : [1, 0, 0, -1],
        },
        {
            "question" : "Si c'est mauvais de grignoter pendant la nuit, à quoi sert la lumière dans le frigo?",
            "choices" : ["Pour faire la fête avant de les manger", "Pour le monstre du frigo", "Pour te faire parler", "Je ne sais pas"],
            "answer" : [1,0,0 ,-1]
        },
        {
            "question" : "Pourquoi met on une pizza qui est ronde dans une boite carrée et la mange-t-on en forme de triangle ?",
            "choices" : ["Laisse moi tranquille", "Stp je suis occupé", "Demande à Pythagore", "Je ne sais pas"],
            "answer" : [1, 1, 1 , -1]
        },
    ], 
    "archibald" : [
         pygame.transform.smoothscale_by(pygame.image.load("assets/images/coworkers/archibald.png"), 0.5),
        {
            "question" : "Ta cravate est trop moche",
            "choices" : ["Je sais", "La tienne aussi", "J'ai pas de cravate aujourd'hui", "T'as la même"],
            "answer" : [0, -1, 1, 1], 
        },
        {
            "question" : "Fait moi un café",
            "choices" : ["Non dsl", "Oui maitre", "*jette ton café dessus*", "Je ne bois pas de café"],
            "answer" : [0, 1, -1, 0],
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
            "question" : "",
            "choices" : [],
            "answer" : "Oui"
        },
    ],
}

def activate(display: pygame.Surface, clock: pygame.time.Clock, FPS: int):

	# Load the background
	bg = pygame.image.load("assets/images/hallway.png")
	bg = pygame.transform.smoothscale(bg, (WIDTH, HEIGHT))
	bg_rect = bg.get_rect()

	# load all the coworkers
	# martin = pygame.image.load("assets/images/coworkers/martin.png")
	# martin = pygame.transform.smoothscale(martin, (WIDTH, HEIGHT))

	# archibald = pygame.image.load("assets/images/coworkers/archibald.png")
	# archibald = pygame.transform.smoothscale(archibald, (WIDTH, HEIGHT))

	# gabriel = pygame.image.load("assets/images/coworkers/gabriel.png")
	# gabriel = pygame.transform.smoothscale(gabriel, (WIDTH, HEIGHT))

	# questions = {
	#	name1 = 
	# }

	# coworker = random.choice([name1, name2, name3])

	#Image to darken
	dark = pygame.Surface((WIDTH, HEIGHT), flags=pygame.SRCALPHA)
	dark.fill((30, 30, 30, 0))
	bg.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
	# Set the initial scale factor
	scale_factor = 1

	# Set the zoom speed
	zoom_speed = 0.005
	scaled_image = bg
	while 1:
		# zoom_speed += 0.0001

		if (scale_factor < 1.5):
			# Increase the scale factor
			scale_factor += zoom_speed
			# Scale the image
			scaled_image = pygame.transform.smoothscale_by(bg, scale_factor)

		# Calculate the position to center the scaled image on the screen
		image_pos = scaled_image.get_rect(center=display.get_rect().center)

		# Draw the scaled image on the screen
		display.blit(scaled_image, image_pos)
		generate_chat_box(display, "SALU C MOI ARCHIBALD LOLOLOLOL", "ARCHIBALD", questions["archibald"][0])
		# generate_multiple_choice(display, ["Oui", "Non", "Peut-être", "Je ne sais pas"])

		time.sleep(0.1)

		upd(clock, FPS)
		end()


def generate_chat_box(display : pygame.Surface, str: str, name, image : pygame.Surface):
	"""
	Function to generate a chat box with a given string composed of multiple lines.
	"""

	generate_background_box(display)
	text_general_offset = 10
	text_vertical_offset = 0
	display.blit(image, (30, CHAT_BOX_TOP - image.get_height()))
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

def render_talk(display : pygame.Surface, Person_data : list):
	"""
	Function to render a discussion between the player and a person.
	"""
	generate_chat_box(display, Person_data[0], Person_data[1], Person_data[2])
	for question in Person_data[3:]:
		generate_multiple_choice(display, question["choices"])

def generate_background_box(display : pygame.Surface):
	Temporary_surface = pygame.Surface((WIDTH, HEIGHT), flags=pygame.SRCALPHA)
	border_color = (255, 255, 255, 255)
	center_color = (30, 30, 30, 170)  # Semi-transparent
	chat_box = pygame.Rect(0, CHAT_BOX_TOP, WIDTH, HEIGHT)
	pygame.draw.rect(Temporary_surface, center_color, chat_box, 0, 10)
	pygame.draw.rect(Temporary_surface, border_color, chat_box, 2, 10)
	display.blit(display, (0, 0))
	pygame.display.update()
