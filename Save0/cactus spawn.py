from util import *

# 成就：仙人掌大师


def row_plant():
	for _ in range(WORLD_SIZE):
		till_to_soil()
		do_water()
		plant(Entities.Cactus)
		move(East)


def row_sort():
	y0 = get_pos_y()
	for x in range(0, WORLD_SIZE - 1):
		moved = False
		move_to(0, y0)
		for _ in range(WORLD_SIZE - 1 - x):
			if measure() > measure(East):
				swap(East)
				moved = True
			move(East)
		if not moved:
			break


def column_sort():
	x0 = get_pos_x()
	for y in range(0, WORLD_SIZE - 1):
		moved = False
		move_to(x0, 0)
		for _ in range(WORLD_SIZE - 1 - y):
			if measure() > measure(North):
				swap(North)
				moved = True
			move(North)
		if not moved:
			break


clear()
while True:
	row_spawn_and_wait_all(row_plant)

	row_spawn_and_wait_all(row_sort)

	column_spawn_and_wait_all(column_sort)

	do_harvest()
