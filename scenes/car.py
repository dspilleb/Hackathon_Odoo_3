from utils import *

import pygame
import random
import time
import os

font = pygame.font.SysFont('VCR_OSD_MONO_1.001.ttf', 40)
#load sprites
pygame.mixer.init()
audio_vache = 'assets/sons/vache.wav'
audio_coffee = 'assets/sons/slurp_coffee.mp3'


COW_SPRITES = [pygame.image.load('assets/images/Odoo_cow/cow0.png'), pygame.image.load('assets/images/Odoo_cow/cow1.png'), pygame.image.load('assets/images/Odoo_cow/cow2.png'), pygame.image.load('assets/images/Odoo_cow/cow3.png')]
Highway_sprite = pygame.image.load('assets/images/Highway.png')
Highway_sprite = pygame.transform.rotate(Highway_sprite, 90)
Highway_sprite = pygame.transform.smoothscale(Highway_sprite, (WIDTH, HEIGHT))
ODOO_BUILDING = pygame.image.load('assets/images/odoo building.png')
ODOO_BUILDING = pygame.transform.smoothscale_by(ODOO_BUILDING, 0.7)
ODOO_COFFEE_SPRITES = pygame.image.load('assets/images/café Odoo.png')
ODOO_COFFEE_SPRITES = pygame.transform.smoothscale_by(ODOO_COFFEE_SPRITES, 0.4)

#avoir plusieurs textures
#accélaration de voiture non linéaire

LINE_THICKNESS = 20

TOTAL_DISTANCE = WIDTH * 7

class Car:
	MAXSPEED = 10
	MULTIPLIER = 1.8
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

class Coffee:
	SPRITE_SIZE_X = ODOO_COFFEE_SPRITES.get_width()
	def __init__(self):
		self.y = float(random.randint(0, HEIGHT - Cow.SPRITE_SIZE))
		self.x = float(random.randint(WIDTH, TOTAL_DISTANCE))
		self.index = 0
		self.sprite = ODOO_COFFEE_SPRITES
		self.mask = pygame.mask.from_surface(self.sprite)

class Final_line:
	def __init__(self):
		self.x = float(TOTAL_DISTANCE)
		self.y = 0.0


def activate(display: pygame.Surface, clock: pygame.time.Clock, FPS: int):
	"""
	\nFunction to play the context of the game"""

	car = Car()
	Cow_list = []
	Coffee_list = []
	final_line = Final_line()
	for i in range(8):
		Cow_list.append(Cow())
	for i in range(3):
		Coffee_list.append(Coffee())

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
		update_cow_position(Cow_list, car)
		update_coffee_position(Coffee_list, car)
		Cow_list = car_collide_cows(car, Cow_list)
		Coffee_list = car_collide_coffee(car, Coffee_list)
		update_final_line_position(final_line, car)
		check_car_win(car, final_line)
		score -= (time.time() - start_time) / 10
		score = max(score, 0)
		display.blit(Highway_sprite, (x, 0))
		display.blit(Highway_sprite, (x - WIDTH, 0))
		draw_final_line(display, final_line)
		display.blit(car.sprite, (car.x, car.y))
		display_cows(display, Cow_list)
		display_cofee(display, Coffee_list)
		render_score(display, score)
		upd(clock, FPS)
	return score

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

sound_played = False

def car_collide_cows(car : Car, Cow_list : list):
	new_Cow_list = []
	for cow in Cow_list:
		offset = (int(cow.x - car.x), int(cow.y - car.y))
		if (car.mask.overlap(cow.mask, offset)):
			car.speed = 0
			if os.path.exists(audio_vache):
				son = pygame.mixer.Sound(audio_vache)
				son.play()

		else:
			new_Cow_list.append(cow)


	return (new_Cow_list)

def car_collide_coffee(car : Car, coffee_list : list):
	new_coffe_list = []
	for coffee in coffee_list:
		offset = (int(coffee.x - car.x), int(coffee.y - car.y))
		if (car.mask.overlap(coffee.mask, offset)):
			car.speed *= Car.MULTIPLIER
			if os.path.exists(audio_coffee):
				son = pygame.mixer.Sound(audio_coffee)
				son.play()
		else:
			new_coffe_list.append(coffee)
	return (new_coffe_list)

def check_car_win(car : Car, final_line : Final_line):
	if (final_line.x <= car.x):
		car.state = 1


def	car_speed(keys : pygame.key.ScancodeWrapper, car : Car):
	if keys[pygame.K_SPACE] and car.speed < Car.MAXSPEED:
				car.speed += Car.ACCELERATION
	else:
		car.speed -= Car.DECELERATION
		if car.speed < Car.MINSPEED:
			car.speed = Car.MINSPEED

def display_cows(display : pygame.Surface, Cow_list : list):
	for cow in Cow_list:
		display.blit(cow.sprite[cow.index % 4], (cow.x, cow.y))
		cow.index += 1
	return

def display_cofee(display : pygame.Surface, Coffee_list : list):
	for coffee in Coffee_list:
		display.blit(coffee.sprite, (coffee.x, coffee.y))
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

def update_coffee_position(Coffee_list : list, car : Car):
	for coff in Coffee_list:
		coff.x -= car.speed
		if coff.x < -Coffee.SPRITE_SIZE_X:
			Coffee_list.remove(coff)
	return

def cow_rotate(cow : Cow):
	for i in range(len(cow.sprite)):
		cow.sprite[i] = pygame.transform.rotate(cow.sprite[i], 180)
	cow.walking_direction = 1 - cow.walking_direction

def render_score (display : pygame.Surface, score : float):
	text = font.render("Score : " + str(int(score)), True, Colors.RED)
	display.blit(text, [0, 0])