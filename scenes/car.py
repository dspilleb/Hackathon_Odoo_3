from utils import *

import pygame
import random
import time

font = pygame.font.SysFont('VCR_OSD_MONO_1.001.ttf', 40)
#load sprites

COW_SPRITES = [pygame.image.load('assets/images/Odoo_cow/cow0.png'), pygame.image.load('assets/images/Odoo_cow/cow1.png'), pygame.image.load('assets/images/Odoo_cow/cow2.png'), pygame.image.load('assets/images/Odoo_cow/cow3.png')]
Highway_sprite = pygame.image.load('assets/images/Highway.png')
Highway_sprite = pygame.transform.rotate(Highway_sprite, 90)
Highway_sprite = pygame.transform.smoothscale(Highway_sprite, (WIDTH, HEIGHT))
ODOO_BUILDING = pygame.image.load('assets/images/odoo building.png')
ODOO_BUILDING = pygame.transform.smoothscale_by(ODOO_BUILDING, 0.7)

#avoir plusieurs textures
#accélaration de voiture non linéaire

LINE_THICKNESS = 20

TOTAL_DISTANCE = WIDTH * 5

class Car:
	MAXSPEED = 10
	MINSPEED = 0
	ACCELERATION = 0.1
	DECELERATION = 0.1
	SIDE_SPEED = 5

	def __init__(self):
		self.speed = 0.0
		self.y = HEIGHT/2
		self.x = WIDTH>>3
		self.state = 0
		self.sprite = pygame.transform.smoothscale_by(pygame.image.load('assets/images/Odoo car.png'), 0.06)
		self.mask = pygame.mask.from_surface(self.sprite)

class Cow:

	SPRITE_SIZE = 128
	HALF_SPRITE_SIZE = SPRITE_SIZE // 2

	def __init__(self):
		self.y = float(random.randint(0, HEIGHT - Cow.SPRITE_SIZE))
		self.x = float(random.randint(WIDTH, TOTAL_DISTANCE))
		self.index = 0
		self.walking_speed = float(random.randint(1, 3))
		self.walking_direction = random.randint(0, 1)
		self.sprite = COW_SPRITES.copy()
		if (self.walking_direction == 1):
			for i in range(len(self.sprite)):
				self.sprite[i] = pygame.transform.rotate(self.sprite[i], 180)
		self.mask = pygame.mask.from_surface(self.sprite[0])

class Final_line:
	def __init__(self):
		self.x = float(TOTAL_DISTANCE)
		self.y = 0.0


def activate(display: pygame.Surface, clock: pygame.time.Clock, FPS: int):
	"""
	\nFunction to play the context of the game"""

	car = Car()
	Cow_list = []
	final_line = Final_line()
	for i in range(8):
		Cow_list.append(Cow())

	x = 0
	score = 1000
	start_time = time.time()
	while not car.state:
		x -= car.speed
		if (x < 0):
			x = WIDTH
		end()
		keys = pygame.key.get_pressed()
		vertical_movement_car(keys, car)
		car_speed(keys, car)
		score -= (time.time() - start_time) / 10
		score = max(score, 0)
		update_informations(display, car, Cow_list, final_line)
		check_car_win(car, final_line)
		render_car_game(display, car, Cow_list, final_line, x)
		upd(clock, FPS)
	
	return score

def render_car_game(display : pygame.Surface, car : Car, Cow_list : list, final_line : Final_line, x : float):
	display.blit(Highway_sprite, (x, 0))
	display.blit(Highway_sprite, (x - WIDTH, 0))
	draw_final_line(display, final_line)
	display.blit(car.sprite, (car.x, car.y))
	display_cows(display, Cow_list)
	return

def update_informations(display : pygame.Surface, car : Car, Cow_list : list, final_line : Final_line):
	update_cow_position(Cow_list, car)
	Cow_list = car_collide_cows(car, Cow_list)
	update_final_line_position(final_line, car)

def draw_final_line(display : pygame.Surface, final_line : Final_line):
	pygame.draw.line(display, Colors.RED, (final_line.x, 0), (final_line.x, HEIGHT), LINE_THICKNESS)
	display.blit(ODOO_BUILDING, (final_line.x + 150, 0))
	return

def update_final_line_position(final_line : Final_line, car : Car):
	final_line.x -= car.speed
	if final_line.x < 0:
		final_line.x = WIDTH
	return

# manage keypresses
def vertical_movement_car(keys : pygame.key.ScancodeWrapper, car : Car):
	if keys[pygame.K_z]:
		car.y -= car.SIDE_SPEED
		if car.y < 0:
			car.y = 0
	elif keys[pygame.K_s]:
		car.y += car.SIDE_SPEED
		if car.y > HEIGHT - car.sprite.get_height():
			car.y = HEIGHT - car.sprite.get_height()
	return

def car_collide_cows(car : Car, Cow_list : list):
	new_Cow_list = []
	for cow in Cow_list:
		offset = (int(cow.x - car.x), int(cow.y - car.y))
		if (car.mask.overlap(cow.mask, offset)):
			car.speed = 0
		else:
			new_Cow_list.append(cow)
	return (new_Cow_list)

def check_car_win(car : Car, final_line : Final_line):
	if (final_line.x <= car.x):
		car.state = 1


def	car_speed(keys : pygame.key.ScancodeWrapper, car : Car):
	if keys[pygame.K_SPACE]:
			car.speed += Car.ACCELERATION
			if car.speed > Car.MAXSPEED:
				car.speed = Car.MAXSPEED
	else:
		car.speed -= Car.DECELERATION
		if car.speed < Car.MINSPEED:
			car.speed = Car.MINSPEED

def display_cows(display : pygame.Surface, Cow_list : list):
	for cow in Cow_list:
		display.blit(cow.sprite[cow.index % 4], (cow.x, cow.y))
		cow.index += 1
	return

def update_cow_position(Cow_list : list, car : Car):
	for cow in Cow_list:
		cow.x -= car.speed
		if cow.x < -Cow.SPRITE_SIZE:
			Cow_list.remove(cow)
		cow.y += cow.walking_speed * (cow.walking_direction * 2 - 1)
		if cow.y < 0:
			cow.y = 0
			cow_rotate(cow)
		elif cow.y > HEIGHT - Cow.SPRITE_SIZE:
			cow.y = HEIGHT - Cow.SPRITE_SIZE
			cow_rotate(cow)
	return

def cow_rotate(cow : Cow):
	for i in range(len(cow.sprite)):
		cow.sprite[i] = pygame.transform.rotate(cow.sprite[i], 180)
	cow.walking_direction = 1 - cow.walking_direction

def render_score (display : pygame.Surface, score : float):
	text = font.render("Score : " + str(int(score)), True, Colors.RED)
	display.blit(text, [0, 0])