from utils import *

import pygame

pygame.init()

# creating window
display = pygame.display.set_mode((WIDTH, HEIGHT))

# creating our frame regulator
clock = pygame.time.Clock()

from scenes import context, office

context.activate(display, clock, FPS)

office.activate(display, clock, FPS)

