from utils import *

import pygame

pygame.init()

# creating window
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Odoo Game")

# creating our frame regulator
clock = pygame.time.Clock()

from scenes import context, office, car, hallway, boss, credits

score = 0

context.activate(display, clock, FPS)

game1 = int(car.activate(display, clock, FPS))
score += game1

game2 = int(office.activate(display, clock, FPS))//3
score += game2

game3 = int(hallway.activate(display, clock, FPS)) * 100
score += game3

print(game1, game2, game3, score)

boss.activate(display, clock, FPS, score)

credits.activate(display, clock, FPS)