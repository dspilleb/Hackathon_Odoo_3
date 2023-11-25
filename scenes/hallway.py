import pygame
from utils import *
import time


def activate(display: pygame.Surface, clock: pygame.time.Clock, FPS: int):

	# Load the image
	image = pygame.image.load("assets/images/hallway.png")
	image = pygame.transform.smoothscale(image, (WIDTH, HEIGHT))
	image_rect = image.get_rect()

	# Set the initial scale factor
	scale_factor = 1

	# Set the zoom speed
	zoom_speed = 0.005

	while 1:
		zoom_speed += 0.0001

		# Increase the scale factor
		scale_factor += zoom_speed

		# Scale the image
		scaled_image = pygame.transform.scale(image, (int(image_rect.width * scale_factor), int(image_rect.height * scale_factor)))

		# Calculate the position to center the scaled image on the screen
		image_pos = scaled_image.get_rect(center=display.get_rect().center)

		# Draw the scaled image on the screen
		display.blit(scaled_image, image_pos)

		time.sleep(0.1)

		upd(clock, FPS)
		end()

