from util import *

def f0():
	# dig all dirt until clay
	while get_ground_type() != Grounds.Clay:
		dig()

def f1():
	
	# exploit all clay unti all rock
	while True:
		rock = 0
		
		for _ in range(WORLD_SIZE):
			
			# grow cycle
			if can_harvest():
				harvest()
			elif get_ground_type() == Grounds.Clay:
				plant(Entities.Rice)
			elif get_ground_type() == Grounds.Dry_Rice_Terrace:
				dig()
			elif get_ground_type() == Grounds.Rock:
				rock += 1
			move(East)

		if rock >= WORLD_SIZE:
			break
	

clear()

while True:
	row_spawn_and_wait_all(to_row_f(f0))
	row_spawn_and_wait_all(to_row_f(f1))
	clear()
