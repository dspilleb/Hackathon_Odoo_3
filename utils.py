import pygame

import sys

from typing import Any
import json

FPS = 30
HEIGHT = 600
WIDTH = 900


class Colors:
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	GRAY = (128, 128, 128)
	BLUE = (0, 0, 255)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	YELLOW = (255, 255, 0)
	GOLD = (255, 215, 0)


def upd(clock: pygame.time.Clock, frames_per_second: int):
	"""
	\nFunction to update the display and tick the clock.
	"""
	pygame.display.flip()
	clock.tick(frames_per_second)


def end():
	"""
	\nFunction to add at the end of every scene.
	\nEnds the game and quits pygame when the users closes the window.
	"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

def get_center_coords(surface: pygame.Surface, *, width=0, height=10) -> tuple[int, int]:
	"""
	Function to center a surface on the screen.
	Horizontal and vertical centering can be disabled by setting the width or height to None.
	"""

	surface_rect = surface.get_rect()

	if width != 0:
		width = WIDTH - surface_rect.width

	if height != 10:
		height = HEIGHT - surface_rect.height

	return width // 2, height // 2


def get_data() -> Any:
	"""Retrieve data from a JSON file using a path."""
	with open("data.json", 'r') as f:
		return json.load(f)


def upd_data(new_data: Any) -> None:
	"""Update data in a JSON file"""
	with open("data.json", 'w') as f:
		json.dump(new_data, f, indent=4)

