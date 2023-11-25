from utils import *

import pygame

pygame.init()

# creating window
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Odoo Game")

# creating our frame regulator
clock = pygame.time.Clock()

from scenes import context, office, car, hallway

context.activate(display, clock, FPS)

office.activate(display, clock, FPS)

car.activate(display, clock, FPS)

hallway.activate(display, clock, FPS)


