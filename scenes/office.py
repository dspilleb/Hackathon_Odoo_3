from utils import *

import pygame



def create_mail(display: pygame.Surface, font: pygame.font.Font, mail_content: str):
    """
    Create a mail with the given content and display it on the screen.
    """
    mail = pygame.draw.rect(display, Colors.WHITE, pygame.Rect(0, 0, 200, 100))  # Create a rectangle for the mail
    mail_text = font.render(mail_content, True, Colors.BLACK)  # Render the mail content
    display.blit(mail_text, (10, 10))  # Display the mail content on the screen
mails = []
txt = ""
#!! so far this just waits for a click
def activate(display: pygame.Surface, clock: pygame.time.Clock, FPS: int):
	"""
	\nFirst mini-game with the office and emails"""
	
	# load the background image
	bg = pygame.image.load('assets/images/bureau.png')
	font = pygame.font.SysFont('Arial', 16)
	#mail = pygame.image.load('assets/images/mail.png')
	mail= pygame.draw.rect(display, Colors.WHITE, pygame.Rect(0, 0, 50, 50))
	while 1:
		display.blit(bg, (0, 0))
		create_mail(display, font, 'This is the content of the mail')  # Create a mail
		upd(clock, FPS)
		# does nothing until click returns the function
		player_input = ""
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				return
			#if event.type == pygame.ENT
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					print("enter")
					
				
			end()
		end()

