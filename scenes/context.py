from utils import *
import time as t
import pygame

# activate shows the bg_filler.png images and the scrolling text

def activate(display: pygame.Surface, clock: pygame.time.Clock, FPS: int):
	"""
	\nFunction to play the context of the game"""
	# scrolling text to explain the game over odoo promotional background music

	# load the background image
	bg = pygame.image.load('assets/images/image.png')
	bg= pygame.transform.scale(bg,(WIDTH,HEIGHT*1.2))
	# use Arial font
	font = pygame.font.SysFont('Algerian', 35)
	# create the text cented horizontally
	text = font.render('This is the context of the game', True, Colors.WHITE)


	# scroll the text from up to down
	text_1 = "Aujourd'hui, marque le début de ton parcours chez Odoo, et comme chaque stagiaire, tu aspires à décrocher une place durable au sein de l'entreprise."
	text_2 = "Cependant, seulement les trois meilleurs auront la chance de transformer ce stage en opportunité concrète."
	text_3 = "Feras-tu partie des heureux élus?"
	text_4 = "Pour le savoir, une règle d'or s'impose dès le départ : ne commettre aucune erreur, à commencer par l'arrivée ponctuelle."

	texts = [text_1, text_2, text_3, text_4]
	for text in texts:
		for i in range(HEIGHT//2):
			# blit dessine l'élément text aux coords 0,i
			display.blit(bg, (0, 0))
			
			#display.blit(text_1, (0, i*3))
			blit_text(display, text, (0, -i*2+200), font,color=Colors.BLACK)
			upd(clock, FPS)
			end()

	return


def blit_text(surface : pygame.Surface, text : str, pos :tuple[int,int] , font : pygame.font.Font, color : tuple[int,int,int]):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size() #size of the window where we display the text
    x, y = pos 
    for line in words:
        for word in line: #check if each word can be put on the same line, if not, go to the next line
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
        
	