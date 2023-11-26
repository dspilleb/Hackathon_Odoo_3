from utils import *

import pygame

import time


data = get_data()

def activate(display: pygame.Surface, clock: pygame.time.Clock, FPS: int, total_score: int):
	"""
		\nFirst mini-game with the office and emails
	"""

	# load the background image
	bg = pygame.image.load('assets/images/coworkers/final_boss.png')
	bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

	font = pygame.font.SysFont('Arial', 25)


	text = font.render(f"Bonsoir, on fait un ping pong?", True, Colors.WHITE)
	text2 = font.render(f"Non, entre ton nom d'abord", True, Colors.WHITE)

	text3 = font.render(f">", True, Colors.WHITE)

	current = ""

	while 1:
		stop = False
		# when the user presses a key, check if it matches the current char
		# if it does, add the char to the current_mail
		# No more comment, code:

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				# enter
				if event.key == 13:
					stop = True
					break
				elif event.key == pygame.K_BACKSPACE:
					current = current[:-1]
				else: 
					current += event.unicode

			# display the text
			display.blit(bg, (0, 0))
			display.blit(text, (100, 200))
			display.blit(text2, (100, 225))
			display.blit(text3, (100, 250))
			name = font.render(current, True, Colors.WHITE)
			display.blit(name, (115,250))

			upd(clock, FPS)

		if stop:
			break
		
	name = current

	data[current] = total_score

	upd_data(data)

	# sort the data
	sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)

	# get the index of the current player
	index = sorted_data.index((name, total_score))

	top1 = sorted_data[0]
	top2 = sorted_data[1]
	top3 = sorted_data[2]

	top1 = font.render(f"{top1[0]} : {top1[1]}", True, Colors.WHITE)
	top2 = font.render(f"{top2[0]} : {top2[1]}", True, Colors.WHITE)
	top3 = font.render(f"{top3[0]} : {top3[1]}", True, Colors.WHITE)


	# leaderboard image
	leaderboard = pygame.image.load('assets/images/leaderboard.png')
	leaderboard = pygame.transform.smoothscale(leaderboard, (WIDTH, HEIGHT))

	fab = pygame.image.load('assets/images/coworkers/fab.png')


	def blit_leaderboard(sorted_data):
		"""
			\nDisplay the leaderboard
		"""

		display.blit(leaderboard, (0, 0))
		display.blit(fab, (400,200))

		display.blit(top1, (255, 215))
		display.blit(top2, (255, 310))
		display.blit(top3, (255, 400))

		top1_name = font.render(f"{sorted_data[0][0]}", True, Colors.WHITE)
		display.blit(top1_name, (446, 508))


	blit_leaderboard(sorted_data)
	upd(clock, FPS)


	txt = font.render(f"Merci pour aujourd'hui {name}", True, Colors.WHITE)
	x = get_center_coords(txt, width=WIDTH)[0]

	blit_leaderboard(sorted_data)
	display.blit(txt, (x, 20))
	upd(clock, FPS)

	time.sleep(3)

	blit_leaderboard(sorted_data)
	txt = font.render(f"Tu as atteint {total_score} points", True, Colors.WHITE)
	x = get_center_coords(txt, width=WIDTH)[0]

	display.blit(txt, (x, 20))
	upd(clock, FPS)

	time.sleep(3)


	blit_leaderboard(sorted_data)
	suffix = "er" if index+1 == 1 else "ème"

	txt = font.render(f"Tu es {index+1}{suffix} sur {len(data.keys())} stagières", True, Colors.WHITE)
	x = get_center_coords(txt, width=WIDTH)[0]

	display.blit(txt, (x, 20))
	upd(clock, FPS)

	time.sleep(3)

	if index+1 == 1:
		blit_leaderboard(sorted_data)
		txt = font.render(f"Tu es le meilleur stagière", True, Colors.WHITE)
		x = get_center_coords(txt, width=WIDTH)[0]

		display.blit(txt, (x, 20))
		upd(clock, FPS)

		time.sleep(3)


		blit_leaderboard(sorted_data)
		txt = font.render(f"Tu as gagné le respect de tes collègues", True, Colors.WHITE)
		x = get_center_coords(txt, width=WIDTH)[0]

		display.blit(txt, (x, 20))
		upd(clock, FPS)

		time.sleep(3)


		blit_leaderboard(sorted_data)
		txt = font.render(f"Et tu as gagné le droit de partir plus tôt", True, Colors.WHITE)
		x = get_center_coords(txt, width=WIDTH)[0]

		display.blit(txt, (x, 20))
		upd(clock, FPS)

		time.sleep(3)


		blit_leaderboard(sorted_data)
		txt = font.render(f"Merci pour ton travail", True, Colors.WHITE)
		x = get_center_coords(txt, width=WIDTH)[0]

		display.blit(txt, (x, 20))
		upd(clock, FPS)

		time.sleep(3)

	elif index+1 in [2, 3]:
		# sélectionné
		blit_leaderboard(sorted_data)
		txt = font.render(f"félicitation! Tu as été embauché, hâte de te revoir", True, Colors.WHITE)
		x = get_center_coords(txt, width=WIDTH)[0]

		display.blit(txt, (x, 20))
		upd(clock, FPS)

		time.sleep(3)

	else : 
		# refusé
		blit_leaderboard(sorted_data)

		txt = font.render(f"Tu n'as pas été embauché, je ne veux plus te voir", True, Colors.WHITE)
		x = get_center_coords(txt, width=WIDTH)[0]
		
		display.blit(txt, (x, 20))
		upd(clock, FPS)

		time.sleep(3)

	blit_leaderboard(sorted_data)
	txt = font.render(f"Tu peux partir maintenant", True, Colors.WHITE)
	x = get_center_coords(txt, width=WIDTH)[0]

	display.blit(txt, (x, 20))
	upd(clock, FPS)

	time.sleep(3)


	blit_leaderboard(sorted_data)
	upd(clock, FPS)

	
	while 1 :
		end()

